#!/usr/bin/bash

MODELS=(
  "Qwen/Qwen2.5-3B"
  "Qwen/Qwen2.5-3B-Instruct"
  "meta-llama/Llama-3.2-3B"
  "meta-llama/Llama-3.2-3B-Instruct"
  "google/gemma-2-2b"
  "google/gemma-2-2b-it"
  "Qwen/Qwen2.5-7B"
  "Qwen/Qwen2.5-7B-Instruct"
  # "meta-llama/Llama-3.1-8B"
  # "meta-llama/Llama-3.1-8B-Instruct"
  # "google/gemma-2-9b"
  # "google/gemma-2-9b-it"
  # "Qwen/Qwen3-4B-Base"
  # "Qwen/Qwen3-4B"
  # "google/gemma-3-4b-pt"
  # "google/gemma-3-4b-it"
  # "Qwen/Qwen3-14B-Base"
  # "Qwen/Qwen3-14B"
  # "google/gemma-3-12b-pt"
  # "google/gemma-3-12b-it"
)

# 2) Iterate over each entry and call your script
for MODEL in "${MODELS[@]}"; do
  echo "=== Model: $MODEL ==="
  python main.py --output_file "results/${MODEL//\//_}_icl_results.csv" --export_latex
done
