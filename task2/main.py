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
    if cache_dir is not None:
        tokenizer = AutoTokenizer.from_pretrained(model_name,cache_dir=cache_dir)

    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Use device_map to shard the model across multiple GPUs
    if cache_dir is not None:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map='auto',
            trust_remote_code=True,
            cache_dir=cache_dir
        ).eval()
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map='auto',
            trust_remote_code=True,
        ).eval()
    return tokenizer, model


def load_data(subset=False):
    df = pd.read_csv('./api_results.csv',sep='|')
    questions = df['question'].tolist()
    formulations = df['formulation_1'].tolist()
    if subset:
        questions = questions[:30]
        formulations = formulations[:30]
    return questions,formulations


def generate_answers(model, tokenizer, questions, formulations, output_path="answers.json", context_prompt=None):
    results = []
    for index, question in enumerate(tqdm(questions)):
        prompt = f"Answer this question with only one sentence: {question}. You should only give the answer in one single sentence.\n\n"
        if context_prompt is not None:
            full_prompt = prompt + "here are some exapmles:\n\n" + context_prompt + f"Q: {question}\nA:"
        else:
            full_prompt = prompt + f"Q: {question}\nA:"

        inputs = tokenizer(full_prompt, return_tensors="pt").to('cuda')
        outputs = model.generate(**inputs, max_new_tokens=200)
        output_ids = [o[len(i):] for i, o in zip(inputs.input_ids, outputs)]
        full_answer = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
        
        answer = full_answer.split('\n\nQ:')[0]
        result = {
            "formulation": formulations[index],
            "answer": answer
        }
        
        results.append(result)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return results

def cal_acc_Qwen(file_path):
    cache_dir = '/export/fs05/dzhang98/models'
    tokenizer,model = load_model_and_tokenizer("Qwen/Qwen3-14B",cache_dir=cache_dir)
    file = open(file_path, 'r')
    data = json.load(file)
    new_file_path = file_path.replace('.json', f'_qwen.json')
    num = 0 
    correct = 0

    if os.path.exists(new_file_path):
        new_data = json.load(open(new_file_path, 'r'))
    else:
        new_data = []
    for index,i in enumerate(tqdm(data)):
        if i['formulation'] in [j['formulation'] for j in new_data]:
            continue
        prompt = f"The event is {i['formulation']}\n\nAnswer: {i['answer']}\n\nIs the event aligned with the answer? Please answer with 'yes' or 'no'\n\n"   
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs_data = model.generate(**inputs,
                max_new_tokens=1,   
                output_scores=True,
                return_dict_in_generate=True,
                top_p = 1,
                top_k = 0,
                temperature=1,
                do_sample=True)
        # yes 9693 no 2152
        outputs = outputs_data.sequences
        scores = outputs_data.scores

        score_yes = scores[0][0,tokenizer.encode('yes')[0]]
        score_no = scores[0][0,tokenizer.encode('no')[0]]
        prob = torch.softmax(torch.tensor([score_yes, score_no]), dim=0)
        output_ids = [o[len(i):] for i, o in zip(inputs.input_ids, outputs)]
        full_answer = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
        num += 1
        if prob[0] > prob[1]:
            correct += 1
        i['llm_answer'] = full_answer
        i['prob'] = prob.tolist()
        new_data.append(i)
        with open(new_file_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
    print(f'Accuracy: {correct/num}')



def cal_acc_openai(file_path,model_name):
    file = open(file_path, 'r')
    data = json.load(file)
    new_file_path = file_path.replace('.json', f'_llm.json')
    print(new_file_path)
    client = OpenAI()

    num = 0 
    correct = 0

    if os.path.exists(new_file_path):
        new_data = json.load(open(new_file_path, 'r'))
    else:
        new_data = []
    for index,i in enumerate(tqdm(data)):
        if i['formulation'] in [j['formulation'] for j in new_data]:

            continue
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
        with open(new_file_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
    

    print(f'Accuracy: {correct/num}')


import random

def enable_icl_for_qa(questions, formulations, n_examples=5, seed=42):

    paired = list(zip(questions, formulations))
    random.seed(seed)
    random.shuffle(paired)

    examples = paired[:n_examples]
    test_data = paired[n_examples:]

    context_prompt = ""
    for q, f in examples:
        context_prompt += f"Q: {q}\nA: {f}\n\n"

    test_questions, test_formulations = zip(*test_data) if test_data else ([], [])
    
    return context_prompt, list(test_questions), list(test_formulations)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    cache_dir = '/export/fs05/dzhang98/models'
    parser.add_argument(
        "--model_name", type=str, help="The Hugging Face model name, required if you want to test the model"
    )
    parser.add_argument(
        "--subset", action="store_true", help="Use a subset of 30 samples for testing"
    )
    parser.add_argument(
        "--eval", action="store_true", help="evaluate the acc for the models"
    )
    parser.add_argument(
        "--icl", action="store_true", help="Use in-context learning prompt"
    )
    args = parser.parse_args()
    if args.eval:
        print("Evaluating model's accuracy")
        #tokenizer, model = load_model_and_tokenizer(args.model_name)
        if not args.icl:
            cal_acc_Qwen(f"{args.model_name.split('/')[-1]}_answers.json")
        else:
            cal_acc_Qwen(f"{args.model_name.split('/')[-1]}_answers_ICL.json")


    else:
        tokenizer, model = load_model_and_tokenizer(args.model_name,cache_dir=cache_dir)
        questions, formulations = load_data(args.subset)
        
        if args.icl:
            context_prompt, questions, formulations = enable_icl_for_qa(questions, formulations)
            answers = generate_answers(model, tokenizer, questions, formulations,
                                   output_path=f"{args.model_name.split('/')[-1]}_answers.json",
                                   context_prompt=context_prompt)
        else:
            answers = generate_answers(model, tokenizer, questions, formulations,
                                   output_path=f"{args.model_name.split('/')[-1]}_answers_ICL.json")


