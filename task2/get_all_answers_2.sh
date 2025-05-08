#!/usr/bin/bash
export CUDA_VISIBLE_DEVICES=0,1

MODELS=(
  # "Qwen/Qwen3-4B-Base"
  "Qwen/Qwen3-4B"
  # "Qwen/Qwen3-14B-Base"
  "Qwen/Qwen3-14B"
)
CUTOFF_DATES=(
  "2024/03/01"
  # "2024/03/01"
  # "2024/03/01"
  "2024/03/01"
)

for i in "${!MODELS[@]}"; do
  MODEL="${MODELS[$i]}"
  CUTOFF="${CUTOFF_DATES[$i]}"
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) eval method: qwen==="
  python main.py --model_name "$MODEL" --eval --eval_method 'qwen'
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) eval method: gemma==="
  python main.py --model_name "$MODEL" --eval --eval_method 'gemma'
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) with ICL eval method: qwen==="
  python main.py --model_name "$MODEL" --icl --eval --eval_method 'qwen'
  echo "=== Running with model: $MODEL (cutoff: $CUTOFF) with ICL eval method: gemma==="
  python main.py --model_name "$MODEL" --icl --eval --eval_method 'gemma'
done

