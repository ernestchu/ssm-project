# Task 2: Time-Conditioned Question Answering


## Quick test

You can run a quick test using a subset of the dataset:

```
python main.py --model_name "your model name" --subset
```

## Generate answers

You can generate answers using the full dataset, with or without in-context learning (ICL).
For ICL, five examples are randomly selected.

To generate answers using the full dataset:
```
python main.py --model_name "your model name" --cache_dir "your cache dir"
```

To generate answers using ICL:
```
python main.py --model_name "your model name" --cache_dir "your cache dir" --icl
```



## Evaluate the model 

We evaluate model outputs using both open-source and closed-source evaluators.

To evaluate with OpenAI:
```
python main.py --model_name "your model name" --eval --eval_method openai --cache_dir "your cache dir" [--icl]
```

To evaluate with Qwen:
```
python main.py --model_name "your model name" --eval --eval_method qwen --cache_dir "your cache dir" [--icl]
```

To evaluate with Gemma:
```
python main.py --model_name "your model name" --eval --eval_method gemma --cache_dir "your cache dir" [--icl]
```
