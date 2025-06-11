import re

with open('site.txt', 'r', encoding='utf-8') as fl:
    cnt = fl.read()

ids = re.findall(r'QuestionId_([A-Za-z0-9]+)', cnt)

unique = list(dict.fromkeys(ids))

with open('test.txt', 'w', encoding='utf-8') as out_fl:
    for index, id_ in enumerate(unique, start=1):
        out_fl.write(f"{index} - {id_}\n")

print(f"Total IDs: {len(unique)}")
print("Done!")