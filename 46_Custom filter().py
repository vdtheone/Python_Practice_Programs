# Custom filter()
"""
Implement a custom version of Python’s built-in filter() function.

Your function should:

Take a predicate function and an iterable as input

Return a new list containing only elements for which the predicate returns True

Input 1
nums = [1, 2, 3, 4, 5, 6]
predicate = is_even

Output 1
[2, 4, 6]

Input 2
words = ["apple", "is", "banana", "kiwi"]
predicate = length_greater_than_3

Output 2
["apple", "banana", "kiwi"]

"""

def custom_filter(func, iterable):
    new_list = []

    for i in iterable:
        if func(i):
            new_list.append(i)

    return new_list

def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
print(custom_filter(is_even, nums))
        
def length_greater_than_3(item):
    count = 0
    for _ in item:
        count+=1
        if count>3:
            return True
    return False

words = ["apple", "is", "banana", "kiwi"]
print(custom_filter(length_greater_than_3, words))
