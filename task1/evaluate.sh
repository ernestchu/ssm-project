#!/usr/bin/bash

MODELS_CUTOFFS=(
  "Qwen/Qwen2.5-3B|2023/12/01"
  "Qwen/Qwen2.5-3B-Instruct|2023/12/01"
  "meta-llama/Llama-3.2-3B|2023/12/01"
  "meta-llama/Llama-3.2-3B-Instruct|2023/12/01"
  "google/gemma-2-2b|2024/06/01"
  "google/gemma-2-2b-it|2024/06/01"
  "Qwen/Qwen2.5-7B|2023/12/01"
  "Qwen/Qwen2.5-7B-Instruct|2023/12/01"
  "meta-llama/Llama-3.1-8B|2023/12/01"
  "meta-llama/Llama-3.1-8B-Instruct|2023/12/01"
  "google/gemma-2-9b|2024/06/01"
  "google/gemma-2-9b-it|2024/06/01"
  "Qwen/Qwen3-4B-Base|2024/03/01"
  "Qwen/Qwen3-4B|2024/03/01"
  "google/gemma-3-4b-pt|2024/08/01"
  "google/gemma-3-4b-it|2024/08/01"
  "Qwen/Qwen3-14B-Base|2024/03/01"
  "Qwen/Qwen3-14B|2024/03/01"
  "google/gemma-3-12b-pt|2024/08/01"
  "google/gemma-3-12b-it|2024/08/01"
)

for pair in "${MODELS_CUTOFFS[@]}"; do
  IFS='|' read -r MODEL CUTOFF <<< "$pair"
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) ==="
  python main.py --model_name "$MODEL" --cutoff_date "$CUTOFF"
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) with ICL ==="
  python main.py --model_name "$MODEL" --cutoff_date "$CUTOFF" --icl
done

