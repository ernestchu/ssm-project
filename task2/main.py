import argparse
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm
from huggingface_hub import login
from datasets import load_dataset
import csv
import os
import json
import random   
from openai import OpenAI
# Load model and tokenizer with model parallelism using device_map
def load_model_and_tokenizer(model_name,cache_dir=None):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Use device_map to shard the model across multiple GPUs
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        trust_remote_code=True,
    ).to("cuda:0").eval()
    return tokenizer, model


def load_data(subset=False):
    df = pd.read_csv('./api_results.csv',sep='|')
    questions = df['question'].tolist()
    formulations = df['formulation_1'].tolist()
    if subset:
        questions = questions[:100]
        formulations = formulations[:100]
    return questions,formulations

def generate_answers(model, tokenizer, questions, formulations, output_path="answers.json"):
    results = []
    for index, question in enumerate(tqdm(questions)):
        prompt = f"Answer this question with only one sentence: {question}. You should only give the answer in one single sentence with no more than 100 words."
        inputs = tokenizer(question, return_tensors="pt").to("cuda")
        outputs = model.generate(**inputs, max_new_tokens=250)

        full_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        if full_answer.startswith(question):
            answer = full_answer[len(question):].strip()
        else:
            answer = full_answer.strip()
        result = {
            "formulation": formulations[index],
            "answer": answer
        }
        results.append(result)

    # 保存为 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return results

def cal_acc(file_path,model_name):
    file = open(file_path, 'r')
    data = json.load(file)

    client = OpenAI()

    num = 0 
    correct = 0
    new_data = []
    for i in tqdm(data):

        prompt = f"The event is {i['formulation']}\n\nAnswer: {i['answer']}\n\nIs the event aligned with the answer? Please answer with 'yes' or 'no'\n\n"   
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )
        num += 1
        if response.output_text.lower() == 'yes':
            correct += 1
        i['llm_answer'] = response.output_text
        new_data.append(i)
    
    new_file_path = file_path.replace('.json', f'_llm.json')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
    print(f'Accuracy: {correct/num}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name", type=str, help="The Hugging Face model name, required if you want to test the model"
    )
    parser.add_argument(
        "--subset", action="store_true", help="Use a subset of 100 samples for testing"
    )
    parser.add_argument(
        "--eval", action="store_true", help="evaluate the acc for the models"
    )
    args = parser.parse_args()
    print("Evaluating model's accuracy")
    if args.eval:
        #tokenizer, model = load_model_and_tokenizer(args.model_name)

        cal_acc(f"{args.model_name.split('/')[-1]}_answers.json",args.model_name)
    else:
        tokenizer, model = load_model_and_tokenizer(args.model_name)
        questions,formulations = load_data(args.subset)
        answers = generate_answers(model, tokenizer, questions,formulations,f"{args.model_name.split('/')[-1]}_answers.json")
