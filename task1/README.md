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
| Metric                          | Qwen/Qwen2.5-3B | Qwen/Qwen2.5-3B-Instruct | meta-llama/Llama-3.2-3B | meta-llama/Llama-3.2-3B-Instruct | google/gemma-2-2b | google/gemma-2-2b-it |
|---------------------------------|------------------|---------------------------|--------------------------|----------------------------------|--------------------|------------------------|
| Year Accuracy                   | 36.51%           | 30.89%                    | 0.05%                    | 10.36%                           | 41.21%             | 35.26%                 |
| Year Month Accuracy             | 10.55%           | 8.47%                     | 0.00%                    | 1.78%                            | 15.05%             | 12.34%                 |
| Year Month Day Accuracy         | 2.07%            | 1.56%                     | 0.00%                    | 0.01%                            | 3.39%              | 1.22%                  |
| Year Month Day +/- 3 Accuracy  | 4.70%            | 3.98%                     | 0.00%                    | 0.35%                            | 7.21%              | 4.50%                  |
| Year Month Day +/- 5 Accuracy  | 5.92%            | 4.79%                     | 0.00%                    | 0.50%                            | 8.47%              | 6.11%                  |
| Year Month Day +/- 10 Accuracy | 8.10%            | 6.50%                     | 0.00%                    | 0.97%                            | 11.40%             | 8.62%                  |

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

