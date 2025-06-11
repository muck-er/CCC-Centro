import re

with open('site.txt', 'r', encoding='utf-8') as file:
    content = file.read()

matches = re.findall(
    r'<span[^>]*data-automation-id="questionOrdinal"[^>]*>(\d+)\.<\/span>.*?QuestionId_([A-Za-z0-9]+)',
    content,
    re.DOTALL
)

sorted_matches = sorted(matches, key=lambda x: int(x[0]))

with open('test2.txt', 'w', encoding='utf-8') as out_file:
    for number, qid in sorted_matches:
        out_file.write(f"{number} - {qid}\n")

print(f"Total matched: {len(sorted_matches)}")
print("Done!")