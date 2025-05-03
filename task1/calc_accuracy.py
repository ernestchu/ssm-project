from argparse import Namespace
from main import main

models = [
    ["Qwen/Qwen2.5-3B", "Qwen2.5-3B"],
    ["Qwen/Qwen2.5-3B-Instruct", "Qwen2.5-3B-it"],
    ["meta-llama/Llama-3.2-3B", "Llama3.2-3B"],
    ["meta-llama/Llama-3.2-3B-Instruct", "Llama3.2-3B-it"],
    ["google/gemma-2-2b", "Gemma2-2B"],
    ["google/gemma-2-2b-it", "Gemma2-2B-it"],
    ["Qwen/Qwen2.5-7B", "Qwen2.5-7B"],
    ["Qwen/Qwen2.5-7B-Instruct", "Qwen2.5-7B-it"],
    # ["meta-llama/Llama-3.1-8B", "Llama3.1-8B"],
    # ["meta-llama/Llama-3.1-8B-Instruct", "Llama3.1-8B-it"],
    # ["google/gemma-2-9b", "Gemma2-9B"],
    # ["google/gemma-2-9b-it", "Gemma2-9B-it"],
    # ["Qwen/Qwen3-4B-Base", "Qwen3-4B"],
    # ["Qwen/Qwen3-4B", "Qwen3-4B-it"],
    # ["google/gemma-3-4b-pt", "Gemma3-4B"],
    # ["google/gemma-3-4b-it", "Gemma3-4B-it"],
    # ["Qwen/Qwen3-14B-Base", "Qwen3-14B"],
    # ["Qwen/Qwen3-14B", "Qwen3-14B-it"],
    # ["google/gemma-3-12b-pt", "Gemma3-12B"],
    # ["google/gemma-3-12b-it", "Gemma3-12B-it"],
]

table = ""
for model_name, model_name_canonical in models:
    res = main(Namespace(
        output_file=f"results/{model_name.replace('/', '_')}_results.csv",
        model_name=None,
    ))
    res_icl = main(Namespace(
        output_file=f"results/{model_name.replace('/', '_')}_icl_results.csv",
        model_name=None,
    ))
    table += f"{model_name_canonical} & "
    for i in range(1, len(res)):
        table += f"{res[i]*100:.2f}/{res_icl[i]*100:.2f} & "
    table = table[:-2]  # Remove the last '& '
    table += "\\\\\n"

print()
print(table)


