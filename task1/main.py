import argparse
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm
from huggingface_hub import login
from datasets import load_dataset
import csv
import os


# Prompt for the task
PROMPT = """Answer in YYYY/MM/DD, on what date was the news about the following event published?
---
{formulation} 

Answer: """
N_ICL_EXAMPLES = 5

# Load model and tokenizer with model parallelism using device_map
def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Use device_map to shard the model across multiple GPUs
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Automatically distribute model across all available GPUs
        offload_folder="./offload",  # Optionally offload to disk if needed
        trust_remote_code=True,
    )
    return tokenizer, model

@torch.no_grad()
def predict_date(model, tokenizer, text):
    '''
    Predict the date of a given text using autoregressive LLM.
    Returns: year, month, day
    '''

    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    # Remove 'token_type_ids' from inputs if it exists (for models like Mistral that don't use it)
    if "token_type_ids" in inputs:
        del inputs["token_type_ids"]

    # Move all inputs to the same device as the model
    inputs = {key: value.to(model.device) for key, value in inputs.items()}

    digit_token_ids = torch.tensor([tokenizer(str(d), add_special_tokens=False)['input_ids'][0] for d in range(10)], device=model.device)
    slash_token_id = tokenizer("/", add_special_tokens=False)["input_ids"][0]
    past_key_values = None
    for i in range(10):
        if i in [4, 7]:  # Add slashes at positions 4 and 7, avoiding extra model inference
            inputs["input_ids"] = torch.cat([inputs["input_ids"], torch.tensor([[slash_token_id]], device=model.device)], dim=1)
            inputs["attention_mask"] = torch.cat([inputs["attention_mask"], torch.ones((1, 1), device=model.device)], dim=1)
            continue
        outputs = model(**inputs) # this adds batch dimension
        past_key_values = outputs.past_key_values
        digit_logits = outputs.logits[:, -1, digit_token_ids]  # Get the logits corresponding to digits for the last token
        pred_digit_token_ids = digit_token_ids[digit_logits.argmax(-1, keepdim=True)]  # Get the predicted digit token ids

        inputs["input_ids"] = torch.cat([inputs["input_ids"], pred_digit_token_ids], dim=1)  # Append the predicted digit token id to the input ids
        inputs["attention_mask"] = torch.cat([inputs["attention_mask"], torch.ones((1, 1), device=model.device)], dim=1)

    pred_date = tokenizer.batch_decode(inputs["input_ids"])[0][-10:]

    return map(int, pred_date.split("/"))


def test_model_on_dataset(model_name, dataset, args):
    tokenizer, model = load_model_and_tokenizer(model_name)

    if args.output_file is None:
        output_file = os.path.join(args.output_dir, f"{model_name.replace('/', '_')}{'_icl' if args.icl else ''}_results.csv")
        os.makedirs(args.output_dir, exist_ok=True)
    else:
        output_file = args.output_file

    # Create CSV file with headers
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "idx",
                "year",
                "month",
                "day",
                "category",
                "model",
                "formulation",
                "input_text",
                "correct_year",
                "correct_month",
                "correct_day",
            ]
        )

        for index, row in tqdm(
            enumerate(dataset), total=len(dataset), desc="Processing events"
        ):
            if args.cutoff_date is not None:
                c_year, c_month, c_day = map(int, args.cutoff_date.split("/"))
                if (
                    row["year"] > c_year
                    or (row["year"] == c_year and row["month"] > c_month)
                    or (row["year"] == c_year and row["month"] == c_month and row["day"] > c_day)
                ):
                    continue
            category = row["category"]  # Category column

            formulations = {
                "original_sentence": row["formulation_1"],
                # "paraphrase_1": row["formulation_2"],
                # "paraphrase_2": row["formulation_3"],
                # "paraphrase_3": row["formulation_4"],
                # "paraphrase_4": row["formulation_5"],
            }

            for key, formulation in formulations.items():
                logprobs = []
                if not formulation.endswith("."):
                    formulation = formulation + "."
                input_text = PROMPT.format(formulation=formulation)
                year, month, day = predict_date(model, tokenizer, input_text)

                logprobs.append(
                    {
                        "year": year,
                        "month": month,
                        "day": day,
                        "input_text": input_text,
                    }
                )

                # Write the results to the CSV file as we go so we don't lose progress in case of a crash
                for logprob_entry in logprobs:
                    writer.writerow(
                        [
                            index,
                            logprob_entry["year"],
                            logprob_entry["month"],
                            logprob_entry["day"],
                            category,
                            model_name,
                            key,
                            logprob_entry["input_text"],
                            row["year"],
                            row["month"],
                            row["day"],
                        ]
                    )

    return output_file


def calculate_accuracy(output_file):
    # Calculate the top-1, top-3, and top-5 accuracy of the model on the original sentences

    # Load the results CSV file
    df = pd.read_csv(output_file)
    num_events = len(df["idx"].unique())

    df = df[df["formulation"] == "original_sentence"]

    correct_y = df[
        (df["year"] == df["correct_year"])
    ]
    correct_ym = df[
        (df["year"] == df["correct_year"])
        & (df["month"] == df["correct_month"])
    ]
    correct_ymd = df[
        (df["year"] == df["correct_year"])
        & (df["month"] == df["correct_month"])
        & (df["day"] == df["correct_day"])
    ]
    correct_ymd3 = df[
        (df["year"] == df["correct_year"])
        & (df["month"] == df["correct_month"])
        & ((df["day"] - df["correct_day"]).abs() <= 3)
    ]
    correct_ymd5 = df[
        (df["year"] == df["correct_year"])
        & (df["month"] == df["correct_month"])
        & ((df["day"] - df["correct_day"]).abs() <= 5)
    ]
    correct_ymd10 = df[
        (df["year"] == df["correct_year"])
        & (df["month"] == df["correct_month"])
        & ((df["day"] - df["correct_day"]).abs() <= 10)
    ]
    y_accuracy = len(correct_y) / num_events
    ym_accuracy = len(correct_ym) / num_events
    ymd_accuracy = len(correct_ymd) / num_events
    ymd3_accuracy = len(correct_ymd3) / num_events
    ymd5_accuracy = len(correct_ymd5) / num_events
    ymd10_accuracy = len(correct_ymd10) / num_events
    
    return y_accuracy, ym_accuracy, ymd_accuracy, ymd3_accuracy, ymd5_accuracy, ymd10_accuracy

def enable_icl(dataset):
    global PROMPT
    # Enable in-context learning (ICL) by adding few-shot examples
    dataset = dataset.shuffle(seed=0)
    examples = dataset.take(N_ICL_EXAMPLES)
    s = PROMPT.split('\n')[0] + "\n---\n"
    for example in examples:
        s += f'{example["formulation_1"]}\n\n'
        s += f'Answer: {example["year"]}/{example["month"]:02}/{example["day"]:02}\n'
        s += "---\n"

    PROMPT = s + '\n'.join(PROMPT.split('\n')[2:])

    # remove the examples from the dataset
    return dataset.skip(N_ICL_EXAMPLES)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name", type=str, help="The Hugging Face model name, required if you want to test the model"
    )
    parser.add_argument(
        "--cutoff_date",
        type=str,
        default=None,
        help="Model knowledge cutoff date in YYYY/MM/DD format",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default=None,
        help="Path to your result CSV file, if provided, the script will not test model again", 
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default='results',
        help="Default directory to save the result CSV files. Would be ignore if output_file is provided",
    )
    parser.add_argument(
        "--subset", action="store_true", help="Use a subset of 100 samples for testing"
    )
    parser.add_argument(
        "--icl", action="store_true", help="Use in-context learning prompt"
    )
    args = parser.parse_args()

    if not args.model_name and not args.output_file:
        raise ValueError("You must provide either --model_name or __output_file")

    if args.output_file and os.path.exists(args.output_file): 
        output_file = args.output_file
    elif args.model_name:
        dataset = load_dataset("hereldav/TimeAware", split="train")
        if args.subset:
            dataset = dataset.shuffle(seed=0).take(100)
        if args.icl:
            dataset = enable_icl(dataset)
        output_file = test_model_on_dataset(args.model_name, dataset, args)
    else:
        raise ValueError("If no result file exists, you must specify --model_name to generate it")

    # calculate accuracy and stability
    y_accuracy, ym_accuracy, ymd_accuracy, ymd3_accuracy, ymd5_accuracy, ymd10_accuracy = calculate_accuracy(output_file)
    print("-" * 40)
    print(f"Year Accuracy: {y_accuracy:.2%}")
    print(f"Year Month Accuracy: {ym_accuracy:.2%}")
    print(f"Year Month Day Accuracy: {ymd_accuracy:.2%}")
    print(f"Year Month Day +/- 3 Accuracy: {ymd3_accuracy:.2%}")
    print(f"Year Month Day +/- 5 Accuracy: {ymd5_accuracy:.2%}")
    print(f"Year Month Day +/- 10 Accuracy: {ymd10_accuracy:.2%}")

    # stability = calculate_stability(output_file)
    # print(f"Stability: {stability:.2%}")
    # print("-" * 40)

if __name__ == "__main__":
    main()
