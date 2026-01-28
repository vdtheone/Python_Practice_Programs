# Check sorted list
"""
Given a list of integers, write a program to check whether the list is sorted in non-decreasing (ascending) order.

Return True if the list is sorted, otherwise return False.

Input 1
nums = [1, 2, 3, 4, 5]

Output 1
True

Input 2
nums = [1, 3, 2, 4]

Output 2
False

Input 3
nums = [5, 5, 7, 9]

Output 3
True

Input 4
nums = [10]

Output 4
True
"""

def check_sorted_list(nums):
    if len(nums)==1:
        return True
    
    for i in range(len(nums)-1):
        if not nums[i]<= nums[i+1]:
            return False
    return True

print("Result = ", check_sorted_list(nums=[1, 2, 3, 4, 5]))
print("Result = ", check_sorted_list(nums=[1, 3, 2, 4]))
print("Result = ", check_sorted_list(nums=[5, 5, 7, 9]))
print("Result = ", check_sorted_list(nums=[10]))


def check_sorted_pythonic(nums):
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

print("Result Pythonic = ", check_sorted_pythonic(nums=[1, 2, 3, 4, 5]))
print("Result Pythonic = ", check_sorted_pythonic(nums=[1, 3, 2, 4]))
print("Result Pythonic = ", check_sorted_pythonic(nums=[5, 5, 7, 9]))
print("Result Pythonic = ", check_sorted_pythonic(nums=[10]))
