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
|-|-|
|Qwen/Qwen3-4B-Base|61.56|63.69|
|Qwen/Qwen3-4B|78.70|91.89|
|google/gemma-3-4b-pt|64.03|70.77|
|google/gemma-3-4b-it|62.18|66.50|
|Qwen/Qwen3-14B-Base|76.57|77.42|
|Qwen/Qwen3-14B|87.83|95.39|
|google/gemma-3-12b-pt|80.98|81.66|
|google/gemma-3-12b-it|79.63|78.60|

# gemma3 12b results

|model|full accuracy|icl accuracy|
|-|-|
|Qwen/Qwen3-4B-Base|89.01|93.27|
|Qwen/Qwen3-4B|69.63|66.51|
|google/gemma-3-4b-pt|91.78|98.22|
|google/gemma-3-4b-it|96.46|98.61|
|Qwen/Qwen3-14B-Base|91.30|95.06|
|Qwen/Qwen3-14B|58.92|62.88|
|google/gemma-3-12b-pt|93.60|98.50|
|google/gemma-3-12b-it|95.63|97.35|
