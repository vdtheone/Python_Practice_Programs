# Count frequency of characters

data = "characters"
counter = {}

for i in data:
    if i in counter:
        counter[i] = counter.get(i) + 1
    else:
        counter[i] = counter.get(i, 1)

print("frequency of characters - ", counter)