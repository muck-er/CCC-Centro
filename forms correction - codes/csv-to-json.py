import pandas as pd
import json

csv_file = pd.read_csv('txt-json/data.csv', delimiter=';')

with open('txt-json/qacc-questions.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

question_to_forms_id = dict(zip(csv_file['question'], csv_file['forms_id']))

for item in json_data:
    pergunta = item.get('question')
    if pergunta in question_to_forms_id:
        item['forms_id'] = question_to_forms_id[pergunta]

with open('txt-json/qacc-questions(updated).json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Created file: qacc-questions(updated).json")
print("Done!")