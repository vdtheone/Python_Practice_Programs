# Remove duplicates from list (keep order)

data = [1,2,3,1,2,2,4,5]

def remove_duplicate(data):
    new_list = []
    seen = {}
    for i in data:
        if i not in seen:
            seen[i] = True
            new_list.append(i)
    return new_list

print(remove_duplicate(data))