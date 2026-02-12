# Count occurrences without using collections

input_str = "vishal"

def count_occurrence(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

print(count_occurrence(input_str))
