# Custom map()

"""
Implement a custom version of Python’s built-in map() function.

Your function should:

Take a function and an iterable as input

Apply the function to each element of the iterable

Return a new list containing the transformed elements

Input 1
nums = [1, 2, 3, 4]
function = square

Output 1
[1, 4, 9, 16]

Input 2
nums = ["a", "bb", "ccc"]
function = length

Output 2
[1, 2, 3]

"""

nums = [1, 2, 3, 4]
strings = ["a", "bb", "ccc"]


def custom_map(func, iterable):
    new_list = []

    for i in iterable:
        new_list.append(func(i))

    return new_list

def square(num):
    return num**2

def length(item):
    count=0
    for _ in item:
        count+=1
    return count

print(custom_map(square, nums))
print(custom_map(length, strings))



