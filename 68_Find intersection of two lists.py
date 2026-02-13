# Find intersection of two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

def find_intersection(list1, list2):
    intersection_set = set(list1) & set(list2)
    return list(intersection_set)

print(find_intersection(list1, list2))