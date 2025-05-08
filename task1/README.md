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
