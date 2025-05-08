# Task 2: Time-Conditioned Question Answering


## Quick test

You can run a quick test using a subset of the dataset:

```
python main.py --model_name "your model name" --subset
```

## Generate answers

You can generate answers using the full dataset, with or without in-context learning (ICL).
For ICL, five examples are randomly selected.

To generate answers using the full dataset:
```
python main.py --model_name "your model name" --cache_dir "your cache dir"
```

To generate answers using ICL:
```
python main.py --model_name "your model name" --cache_dir "your cache dir" --icl
```



## Evaluate the model 

We evaluate model outputs using both open-source and closed-source evaluators.

To evaluate with OpenAI:
```
python main.py --model_name "your model name" --eval --eval_method openai --cache_dir "your cache dir" [--icl]
```

To evaluate with Qwen:
```
python main.py --model_name "your model name" --eval --eval_method qwen --cache_dir "your cache dir" [--icl]
```

To evaluate with Gemma:
```
python main.py --model_name "your model name" --eval --eval_method gemma --cache_dir "your cache dir" [--icl]
```

## GPT results

We use GPT-4o-mini to systematically assess the alignment between model-generated responses and ground-truth formulations.

|model|accuracy|
|-|-|
|Qwen/Qwen2.5-3B|35.96|
|Qwen/Qwen2.5-3B-Instruct|30.28|
|meta-llama/Llama-3.2-3B|48.32|
|meta-llama/Llama-3.2-3B-Instruct|41.36|
|google/gemma-2-2b|23.72|
|google/gemma-2-2b-it|41.86|

## Qwen3-14B resutls

Evaluation is based on the log-probabilities of the generated tokens "Yes"/"No".

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

Evaluation is based on the log-probabilities of the generated tokens "True"/"False".

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
