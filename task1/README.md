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
| Zero-shot/ICL     | Qwen/Qwen2.5-3B | Qwen/Qwen2.5-3B-Instruct | meta-llama/Llama-3.2-3B | meta-llama/Llama-3.2-3B-Instruct | google/gemma-2-2b | google/gemma-2-2b-it |
|---------------------------------|------------------|---------------------------|--------------------------|----------------------------------|--------------------|------------------------|
| Year Accuracy                   | 36.51/39.05          | 30.89/37.04                    | 0.05/11.52                    | 10.36/3.09                           | 41.21/49.34             | 35.26/46.66                 |
| Year Month Accuracy             | 10.55/12.41          | 8.47/10.46                     | 0.00/0.55                    | 1.78/0.16                            | 15.05/19.15             | 12.34/16.63                 |
| Year Month Day Accuracy         | 2.07/2.94           | 1.56/2.60                     | 0.00/0.04                    | 0.01/0.02                            | 3.39/7.14              | 1.22/4.78                  |
| Year Month Day +/- 3 Accuracy  | 4.70/5.86          | 3.98/5.30                     | 0.00/0.11                    | 0.35/0.02                            | 7.21/11.52              | 4.50/8.96                  |
| Year Month Day +/- 5 Accuracy  | 5.92/7.32          | 4.79/6.43                     | 0.00/0.12                    | 0.50/0.04                            | 8.47/12.80              | 6.11/10.38                  |
| Year Month Day +/- 10 Accuracy | 8.10/9.56          | 6.50/8.35                     | 0.00/0.29                    | 0.97/0.06                            | 11.40/15.65             | 8.62/12.96                  |

