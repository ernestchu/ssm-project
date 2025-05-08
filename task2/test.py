import json
path = '/home/dzhang98/code/ssm-project/task2/gemma-3-4b-it_answers_full_gemma.json'
file = open(path,'r')

data = json.load(file)
cnt = 0
acc = 0
for i in data:
    prob = i['prob']
    if prob[0] > prob[1]:
        acc += 1
    cnt += 1

print(acc/cnt)