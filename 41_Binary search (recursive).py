# Binary search (recursive)

data = [1,2,3,4,5,6,7,8,9,10]

def binary_search(data, search_element):
    left, right = 0, len(data)-1

    while left<=right:
        mid = (left+right)//2
        if data[mid] == search_element:
            return f"{search_element} is placed on index {mid}"
        if search_element > data[mid]:
            left = mid + 1
        elif search_element < data[mid]:
            right = mid -1

    return "Element not found"

print("Result = ", binary_search(data, search_element=6))
print("Result = ", binary_search(data, search_element=2))
print("Result = ", binary_search(data, search_element=4))
print("Result = ", binary_search(data, search_element=10))
print("Result = ", binary_search(data, search_element=5))



def binary_search_recursive(data, target, left, right, count=1):
    if left>right:
        return -1
    
    mid = (left+right)//2

    if data[mid] == target:
        return mid
    elif target > data[mid]:
        return binary_search_recursive(data, target, left+1, right, count=count+1)
    else:
        return binary_search_recursive(data, target, left, right-1, count=count+1)
print("Recursive Result = ", binary_search_recursive(data, 6, 0, 9))
print("Recursive Result = ", binary_search_recursive(data, 2, 0, 9))
print("Recursive Result = ", binary_search_recursive(data, 4, 0, 9))
print("Recursive Result = ", binary_search_recursive(data, 10, 0, 9))
print("Recursive Result = ", binary_search_recursive(data, 5, 0, 9))

