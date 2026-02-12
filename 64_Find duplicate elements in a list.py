# Find duplicate elements in a list

data = [1,2,3,4,3,2,4,5,6,7,7,8]

def find_duplicates(data):
    seen = set()
    duplicates = []
    for i in data:
        if i in seen and i not in duplicates:
            duplicates.append(i)
        else:
            seen.add(i)
    return duplicates

print(find_duplicates(data))