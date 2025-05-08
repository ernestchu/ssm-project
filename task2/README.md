# Task 2: Time-Conditioned Question Answering


## Quick test

You can use subset to test the data.
```
python main.py --model_name "your model name" --subset
```

## Generate answers


Generate the LLMs' answer for full dataset.
```
python main.py --model_name "your model name" --cache_dir "your cache dir"
```

Generate the LLMs' answer for ICL test.
```
python main.py --model_name "your model name" --cache_dir "your cache dir" --icl
```



## Evaluate the model 

We use open-source models to evaluate the results. Here are the commands.

Call OpenAI API to evaluate the result.
```
python main.py --model_name "your model name" --eval --eval_method openai --cache_dir "your cache dir" [--icl]
```

Use Qwen to evaluate the result
```
python main.py --model_name "your model name" --eval --eval_method qwen --cache_dir "your cache dir" [--icl]
```

Use Gemma to evaluate the result
```
python main.py --model_name "your model name" --eval --eval_method gemma --cache_dir "your cache dir" [--icl]
```

## GPT results

We aim to systematically assess the alignment between the large model's responses and the corresponding formulations. For this evaluation, we employ GPT-4o-mini as the judgment model.

|model|accuracy|
|-|-|
|Qwen/Qwen2.5-3B|35.96|
|Qwen/Qwen2.5-3B-Instruct|30.28|
|meta-llama/Llama-3.2-3B|48.32|
|meta-llama/Llama-3.2-3B-Instruct|41.36|
|google/gemma-2-2b|23.72|
|google/gemma-2-2b-it|41.86|

## Qwen3-14B resutls


|model|full accuracy|icl accuracy|
|-|-|-|
|Qwen/Qwen3-4B-Base|61.56|63.69|
|Qwen/Qwen3-4B|62.57|61.91|
|google/gemma-3-4b-pt|64.03|70.77|
|google/gemma-3-4b-it|62.18|66.50|
|Qwen/Qwen3-14B-Base|76.57|77.42|
|Qwen/Qwen3-14B|76.78|80.05|
|google/gemma-3-12b-pt|80.98|81.66|
|google/gemma-3-12b-it|79.63|78.60|

# Gemma3-12B results

|model|full accuracy|icl accuracy|
|-|-|-|
|Qwen/Qwen3-4B-Base|89.01|93.27|
|Qwen/Qwen3-4B|96.51|94.42|
|google/gemma-3-4b-pt|91.78|98.22|
|google/gemma-3-4b-it|96.46|98.61|
|Qwen/Qwen3-14B-Base|91.30|95.06|
|Qwen/Qwen3-14B|86.06|95.13|
|google/gemma-3-12b-pt|93.60|98.50|
|google/gemma-3-12b-it|95.63|97.35|
