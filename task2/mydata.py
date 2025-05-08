import json

path = '/home/dzhang98/code/ssm-project/task2/Qwen3-4B_answers_full_gemma.json'
file = open(path,'r')

data = json.load(file)
print(len(data))

cnt = 0
acc = 0
for i in data:
    prob = i['prob']
    if prob[0] > prob[1]:
        acc += 1
    cnt += 1

print(acc/cnt)