import re

question_ids = []


with open('site.txt', 'r', encoding='utf-8') as fl:
    cnt = fl.read()

ids = re.findall(r'QuestionId_([A-Za-z0-9]+)', cnt)

unique = list(set(ids))

with open('extracted_ids.txt', 'w', encoding='utf-8') as out_fl:
    for id_ in unique:
        out_fl.write(id_ + '\n')

print(f"Total ID's: {len(unique)}")
print("Done!")