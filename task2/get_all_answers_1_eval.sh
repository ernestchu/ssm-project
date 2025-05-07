#!/usr/bin/bash

MODELS=(
  "Qwen/Qwen3-4B-Base"
  "Qwen/Qwen3-4B"
  "google/gemma-3-4b-pt"
  "google/gemma-3-4b-it"
  "Qwen/Qwen3-14B-Base"
  "Qwen/Qwen3-14B"
  "google/gemma-3-12b-pt"
  "google/gemma-3-12b-it"
)
CUTOFF_DATES=(
  "2024/03/01"
  "2024/03/01"
  "2024/08/01"
  "2024/08/01"
  "2024/03/01"
  "2024/03/01"
  "2024/08/01"
  "2024/08/01"
)

for i in "${!MODELS[@]}"; do
  MODEL="${MODELS[$i]}"
  CUTOFF="${CUTOFF_DATES[$i]}"
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) ==="
  python main.py --model_name "$MODEL" --eval
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) with ICL ==="
  python main.py --model_name "$MODEL" --icl --eval
done

