# Flatten nested list

data = [[1, 2], [3, [4, 5]]]

def flatten_nested_list(data):
    new_list = []
    for i in data:
        if isinstance(i, list):
            new_list.extend(flatten_nested_list(i))
        else:
            new_list.append(i)
    return new_list

print(flatten_nested_list(data))