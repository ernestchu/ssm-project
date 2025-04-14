# ssm-project

|Model|Base|Instruct|
|-|-|-|
|Qwen-2.5 3B|https://huggingface.co/Qwen/Qwen2.5-3B|https://huggingface.co/Qwen/Qwen2.5-3B-Instruct|
|Llama-3.2 3B|https://huggingface.co/meta-llama/Llama-3.2-3B|https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct|
|Gemma-2 2B|https://huggingface.co/google/gemma-2-2b|https://huggingface.co/google/gemma-2-2b-it|

### TODO list
- [ ] Task 1 (assignee: Ernie)
- [ ] Task 2
  - [ ] Generate QA pairs using GPT4o  (assignee: )
  - [ ] Run evaluation  (assignee: )

### Metrics



**Task 1: Date Extraction Accuracy Evaluation**

**Prompt:(you can change the prompt to make the answer more stable)**  
*Given the Event: {EVENT}. Can you tell me when this event happened? You need to provide the answer in the format YYYY/MM/DD.*

After collecting model responses, compute the accuracy for each component of the date—**year**, **month**, and **day**—separately.

---

**Task 2: Factual Consistency Evaluation**

For the GPT-4o evaluation, the data format is as follows:

- **Event:** Croatia adopts the euro and joins the Schengen Area. (2023/01/01)  
- **Question:** What major economic and travel-related changes did Croatia implement on January 1, 2023?  
- **Answer:** On January 1, 2023, Croatia adopted the euro as its official currency and joined the Schengen Area.

Feed only the **question** to the LLMs and collect their responses. Then evaluate whether the model’s generated answer faithfully reflects the information in the **event** description.



### Useful links
- [TimeAware Dataset](https://huggingface.co/datasets/hereldav/TimeAware)
- [TimeAware Dataset paper](https://arxiv.org/abs/2409.13338)
- [TimeAware Dataset code](https://github.com/vojtechbartek/timeaware)
