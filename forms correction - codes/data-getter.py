import re

with open('site.txt', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = re.findall(
    r'<div id="QuestionId_([a-zA-Z0-9]+)".*?>.*?'
    r'<span[^>]+data-automation-id="questionOrdinal"[^>]*>\s*(\d+)\.\s*</span>.*?'
    r'<span[^>]*class="[^"]*text-format-content[^"]*"[^>]*>(.*?)</span>',
    content,
    re.DOTALL
)

print(f"Total found: {len(pattern)}")

sorted_data = sorted(pattern, key=lambda x: int(x[1]))

with open('full_questions_with_ids.txt', 'w', encoding='utf-8') as out:
    for qid, number, question in sorted_data:
        cleaned_question = re.sub(r'\s+', ' ', question).strip()
        out.write(f"{number} - {qid} - {cleaned_question}\n")