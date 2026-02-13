# Remove elements appearing more than twice

def remove_elements_appearing_more_than_twice(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    result = []
    for item in lst:
        if count[item] <= 2:
            result.append(item)
    return result 

print(remove_elements_appearing_more_than_twice([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]))