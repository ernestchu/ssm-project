# A Fairer Evaluation for the Time Awareness in Instruction-Tuned LLMs

| [Tech Report](tech-report.pdf) | [Poster](poster.pdf) |
|-|-|


[Ernie Chu](https://www.cs.jhu.edu/~schu23/), Junhyeok Lee, Dengjia Zhang. Johns Hopkins University.

---

When asked "Who is the President?", a model's answer must depend on time. Yet most evaluations ignore this. Temporal awareness is a critical and under-evaluated capability of large language models (LLMs), especially for real-world applications where factual accuracy depends on the referenced date. Existing benchmarks such as TimeShift assess temporal reasoning by comparing log probabilities of dated statements, favoring base models tuned for next-token prediction. In this work, we introduce a question-answering-based evaluation framework designed to fairly assess temporal reasoning in instruction-tuned LLMs. Our approach builds on the TimeAware dataset and includes two tasks: (1) precise date prediction and (2) time-conditioned factual question answering. We evaluate a range of open-source LLMs, including both base and instruction-tuned variants, under zero-shot and in-context settings, using strong LLMs as automated judges. Results show that instruction-tuned models lag behind base models in date prediction but perform competitively in question-answering, especially with few-shot prompting. These findings highlight a trade-off introduced by instruction tuning and motivate the need for evaluation protocols and training methods that preserve temporal knowledge in instruction-optimized models.

## Main Evaluation

### Environment setup:
```sh
conda create -n ssm-proj python=3.10 -y
pip install -r requirements.txt
```

(Optionally) [Log in](https://huggingface.co/docs/huggingface_hub/en/guides/cli#huggingface-cli-login) with a Hugging Face account to gain access to gated models
```sh
huggingface-cli login
```


[**Task 1: Precise Date Prediction.**](task1)


This task evaluates the LLM's ability to directly predict the date of an event given its description. We formulate the input as a prompt asking the LLM to provide the date in YYYY/MM/DD format. Please refere to our tech report for the specific procedure.


**[Task 2: Time-Conditioned Question Answering](task2)**

This task simulates real-world user interactions by posing factual questions about events within specific temporal contexts. It aims to evaluate the LLM's ability to provide accurate and contextually relevant answers. Please refere to our tech report for the specific procedure.


## List of models we tested on
- [Tiny standard (old) model](#tiny-standard-old-model)
- [Small standard (old) model](#small-standard-old-model)
- [Tiny Latest model](#tiny-latest-model)
- [Small Latest model](#small-latest-model)
  
### Tiny standard (old) model
|Model|Base|Instruct|Cut-off Date|
|-|-|-|-|
|Qwen-2.5 3B|[Qwen/Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B)|[Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)|2023/12/01|
|Llama-3.2 3B|[meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B)|[meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)|2023/12/01|
|Gemma-2 2B|[google/gemma-2-2b](https://huggingface.co/google/gemma-2-2b)|[google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)|2024/06/01|

### Small standard (old) model
|Model|Base|Instruct|Cut-off Date|
|-|-|-|-|
|Qwen-2.5 7B|[Qwen/Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B)|[Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)|2023/12/01|
|Llama-3.1 8B|[meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B)|[meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)|2023/12/01|
|Gemma-2 9B|[google/gemma-2-9b](https://huggingface.co/google/gemma-2-9b)|[google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)|2024/06/01|


### Tiny Latest model
|Model|Base|Instruct|Cut-off Date|
|-|-|-|-|
|Qwen-3 4B|[Qwen/Qwen3-4B-Base](https://huggingface.co/Qwen/Qwen3-4B-Base)|[Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)|2024/03/01|
|Gemma-3 4B|[google/gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)|[google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it)|2024/08/01|

### Small Latest model
|Model|Base|Instruct|Cut-off Date|
|-|-|-|-|
|Qwen-3 14B|[Qwen/Qwen3-14B-Base](https://huggingface.co/Qwen/Qwen3-14B-Base)|[Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)|2024/03/01|
|Gemma-2 12B|[google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)|[google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it)|2024/08/01|


### Useful links
- [TimeAware Dataset](https://huggingface.co/datasets/hereldav/TimeAware)
- [TimeAware Dataset paper](https://arxiv.org/abs/2409.13338)
- [TimeAware Dataset code](https://github.com/vojtechbartek/timeaware)
