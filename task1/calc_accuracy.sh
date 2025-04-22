#!/usr/bin/bash

MODELS=(
  "Qwen/Qwen2.5-3B"
  "Qwen/Qwen2.5-3B-Instruct"
  "meta-llama/Llama-3.2-3B"
  "meta-llama/Llama-3.2-3B-Instruct"
  "google/gemma-2-2b"
  "google/gemma-2-2b-it"
)

# 2) Iterate over each entry and call your script
for MODEL in "${MODELS[@]}"; do
  echo "=== Model: $MODEL ==="
  python main.py --output_file "results/${MODEL//\//_}_results.csv"
done
