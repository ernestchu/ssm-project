# Task 2: Time-Conditioned Question Answering


## quick start


Generate the LLMs' answer.
```
python main.py --model_name Qwen/Qwen2.5-3B
```

Call OpenAI API to test the result.
```
python main.py --model_name Qwen/Qwen2.5-3B --eval 
```

## results

We aim to systematically assess the alignment between the large model's responses and the corresponding formulations. For this evaluation, we employ GPT-4o-mini as the judgment model.

|model|accuracy|
|-|-|
|Qwen/Qwen2.5-3B|0.3596|
|Qwen/Qwen2.5-3B-Instruct|0.3028|
|meta-llama/Llama-3.2-3B|48.32|
|meta-llama/Llama-3.2-3B-Instruct||
|google/gemma-2-2b|23.72|
|google/gemma-2-2b-it||

## next step

We will use some open source LLMs to test wheter the answer and formulation are aligned. 
