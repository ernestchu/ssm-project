from datasets import load_dataset
from openai import OpenAI
import random
import csv
from tqdm import tqdm
ds = load_dataset("hereldav/TimeAware", split="train")

# sample data
# {'formulation_1': "Claudine Gay, Harvard University's first Black president, resigns following testimony to Congress on anti-semitism and amid plagiarism allegations.", 'formulation_2': "Claudine Gay, who made history as Harvard University's first Black president, stepped down after testifying before Congress about anti-Semitism and facing accusations of plagiarism.", 'formulation_3': 'The first Black president of Harvard University, Claudine Gay, has resigned after providing testimony to Congress regarding anti-Semitism and in the wake of plagiarism claims.', 'formulation_4': "After testifying to Congress on the issue of anti-Semitism and dealing with allegations of plagiarism, Claudine Gay, Harvard's inaugural Black president, has resigned.", 'formulation_5': "Claudine Gay resigned as Harvard University's first Black president after her Congressional testimony on anti-Semitism and amid allegations of plagiarism.", 'year': 2024, 'month': 1, 'day': 2, 'category': 'Politics & Government', 'reference': 'https://www.nature.com/articles/d41586-024-00009-8', 'country': 'United States', 'continent': 'North America'}
# open csv file
# open existing csv file
with open('timeaware.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='|')
    existing_items = list(reader)

client = OpenAI()
with open('timeaware.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['formulation_1', 'formulation_2', 'formulation_3', 'formulation_4', 'formulation_5', 'year', 'month', 'day', 'category', 'reference', 'country', 'continent', 'question'], delimiter='|')
    writer.writeheader()
    iterator = iter(ds)
    for i, item in tqdm(enumerate(existing_items)):
        writer.writerow(item)
    for i, item in tqdm(enumerate(iterator)):
        if i< len(existing_items):
            continue
        
        # select a random formulation between 1 and 5
        # it is assgigned in dict
        formulation = random.choice([item['formulation_1'], item['formulation_2'], item['formulation_3'], item['formulation_4'], item['formulation_5']])
        prompt = f"At {item['year']}-{item['month']}-{item['day']}, the event \"{item['formulation_1']}\" happened in {item['country']}, {item['continent']} which is related to {item['category']}. Can you ask a time-aware question that would lead to this event as the answer?"

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        question = response.output_text
        item['question'] = question
        writer.writerow(item)
