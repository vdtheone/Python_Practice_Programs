# Find union of two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

def find_union(list1, list2):
    union_set = set(list1) | set(list2)
    return list(union_set)

print(find_union(list1, list2)) 