# Find common elements in two lists

list_1 = [8, 1, 2, 2, 3, 4, 5, 6]
list_2 = [8, 2, 2, 4, 6, 5]

output = [2, 4]

print("common_elements_without_preserve_order : ",list((set(list_1).intersection(set(list_2)))))
print("common_elements_without_preserve_order : ",list(set(list_1) & set(list_2)))

def common_elements_preserve_order(list1, list2):
    set2 = set(list2)
    result = []
    seen = set()

    for i in list1:
        if i in set2 and i not in seen:
            result.append(i)
            seen.add(i)
    
    return result

print("common_elements_preserve_order : ",common_elements_preserve_order(list_1, list_2))