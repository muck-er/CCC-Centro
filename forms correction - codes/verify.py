with open('extracted_ids.txt') as f:
    ids = [line.strip() for line in f]

duplicates = set([x for x in ids if ids.count(x) > 1])

if duplicates:
    print("Repeated IDs:")
    for d in duplicates:
        print(d)
else:
    print("No repeated IDs.")
