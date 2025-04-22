# Task 1

### TODO
- drop data beyond models' cut-off date
- ICL (prepend examples QA to the prompt)

### Quick Start
Environment setup:
```sh
conda create -n ssm-proj python=3.10 -y
pip install -r requirements.txt
```

(Optionally) [Log in](https://huggingface.co/docs/huggingface_hub/en/guides/cli#huggingface-cli-login) with a Hugging Face account to gain access to gated models
```sh
huggingface-cli login
```

Benchmark a Hugging Face model on TimeAware (you can pass `--subset` for a quick test):

```bash
python main.py --model_name <Hugging Face model name>
```

Calculate scores for already tested model:

```bash
python main.py --output_file <path to results file>
```

### Results on full dataset
```
=== Model: Qwen/Qwen2.5-3B ===
----------------------------------------
Year Accuracy: 36.51%
Year Month Accuracy: 10.55%
Year Month Day Accuracy: 2.07%
Year Month Day +/- 3 Accuracy: 4.70%
Year Month Day +/- 5 Accuracy: 5.92%
Year Month Day +/- 10 Accuracy: 8.10%
=== Model: Qwen/Qwen2.5-3B-Instruct ===
----------------------------------------
Year Accuracy: 30.89%
Year Month Accuracy: 8.47%
Year Month Day Accuracy: 1.56%
Year Month Day +/- 3 Accuracy: 3.98%
Year Month Day +/- 5 Accuracy: 4.79%
Year Month Day +/- 10 Accuracy: 6.50%
=== Model: meta-llama/Llama-3.2-3B ===
----------------------------------------
Year Accuracy: 0.05%
Year Month Accuracy: 0.00%
Year Month Day Accuracy: 0.00%
Year Month Day +/- 3 Accuracy: 0.00%
Year Month Day +/- 5 Accuracy: 0.00%
Year Month Day +/- 10 Accuracy: 0.00%
=== Model: meta-llama/Llama-3.2-3B-Instruct ===
----------------------------------------
Year Accuracy: 10.36%
Year Month Accuracy: 1.78%
Year Month Day Accuracy: 0.01%
Year Month Day +/- 3 Accuracy: 0.35%
Year Month Day +/- 5 Accuracy: 0.50%
Year Month Day +/- 10 Accuracy: 0.97%
=== Model: google/gemma-2-2b ===
----------------------------------------
Year Accuracy: 41.21%
Year Month Accuracy: 15.05%
Year Month Day Accuracy: 3.39%
Year Month Day +/- 3 Accuracy: 7.21%
Year Month Day +/- 5 Accuracy: 8.47%
Year Month Day +/- 10 Accuracy: 11.40%
=== Model: google/gemma-2-2b-it ===
----------------------------------------
Year Accuracy: 35.26%
Year Month Accuracy: 12.34%
Year Month Day Accuracy: 1.22%
Year Month Day +/- 3 Accuracy: 4.50%
Year Month Day +/- 5 Accuracy: 6.11%
Year Month Day +/- 10 Accuracy: 8.62%
```

### Results on 1k subset
```
=== Model: Qwen/Qwen2.5-3B ===
----------------------------------------
Year Accuracy: 33.00%
Year Month Accuracy: 8.00%
Year Month Day Accuracy: 0.00%
Year Month Day +/- 3 Accuracy: 4.00%
Year Month Day +/- 5 Accuracy: 5.00%
Year Month Day +/- 10 Accuracy: 6.00%
=== Model: Qwen/Qwen2.5-3B-Instruct ===
----------------------------------------
Year Accuracy: 35.00%
Year Month Accuracy: 9.00%
Year Month Day Accuracy: 2.00%
Year Month Day +/- 3 Accuracy: 5.00%
Year Month Day +/- 5 Accuracy: 6.00%
Year Month Day +/- 10 Accuracy: 6.00%
=== Model: meta-llama/Llama-3.2-3B ===
----------------------------------------
Year Accuracy: 0.00%
Year Month Accuracy: 0.00%
Year Month Day Accuracy: 0.00%
Year Month Day +/- 3 Accuracy: 0.00%
Year Month Day +/- 5 Accuracy: 0.00%
Year Month Day +/- 10 Accuracy: 0.00%
=== Model: meta-llama/Llama-3.2-3B-Instruct ===
----------------------------------------
Year Accuracy: 4.00%
Year Month Accuracy: 1.00%
Year Month Day Accuracy: 0.00%
Year Month Day +/- 3 Accuracy: 1.00%
Year Month Day +/- 5 Accuracy: 1.00%
Year Month Day +/- 10 Accuracy: 1.00%
=== Model: google/gemma-2-2b ===
----------------------------------------
Year Accuracy: 38.00%
Year Month Accuracy: 10.00%
Year Month Day Accuracy: 1.00%
Year Month Day +/- 3 Accuracy: 4.00%
Year Month Day +/- 5 Accuracy: 5.00%
Year Month Day +/- 10 Accuracy: 8.00%
=== Model: google/gemma-2-2b-it ===
----------------------------------------
Year Accuracy: 35.00%
Year Month Accuracy: 11.00%
Year Month Day Accuracy: 0.00%
Year Month Day +/- 3 Accuracy: 1.00%
Year Month Day +/- 5 Accuracy: 3.00%
Year Month Day +/- 10 Accuracy: 7.00%
```

