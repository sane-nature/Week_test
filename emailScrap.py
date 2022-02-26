import json
import re

file = open('websiteData.txt', 'r+')

dict = {}
human_email = []
non_human_email = []
for line in file:
    words = line.split(' ')
    for word in words:
        human_email = human_email+re.findall(r"[a-z]+\.[a-z0-9]+@[\w]+\.[a-z]{2,3}", word)
        non_human_email = non_human_email +re.findall(r"^[\w]{2,8}@[\w]+\.[a-z]{2,3}", word)

human = list(set(human_email))
non_human = list(set(non_human_email))

num=0
for i in human:
    dict[i] = {"Occurrence": human_email.count(i), "EmailType": "Human"}
    num=num+1


for i in non_human:
    dict[i] = {"Occurrence": non_human_email.count(i), "EmailType": "Non-Human"}
    num=num+1

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, ensure_ascii=False, indent=4)