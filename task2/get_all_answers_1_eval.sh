#!/usr/bin/bash

MODELS=(
  # "Qwen/Qwen3-4B-Base"
  "Qwen/Qwen3-4B"
  "Qwen/Qwen3-14B-Base"
  # "Qwen/Qwen3-14B"
)
CUTOFF_DATES=(
  "2024/03/01"
  "2024/03/01"
)

for i in "${!MODELS[@]}"; do
  MODEL="${MODELS[$i]}"
  CUTOFF="${CUTOFF_DATES[$i]}"
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) ==="
  python main.py --model_name "$MODEL" --eval
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) with ICL ==="
  python main.py --model_name "$MODEL" --icl --eval
done

