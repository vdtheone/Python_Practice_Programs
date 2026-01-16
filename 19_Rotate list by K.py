# Rotate list by K

"""
    Problem Statement:
    You are given a list of elements and an integer K.
    Write a program to rotate the list to the right by K positions.
"""

input_list = [1, 2, 3, 4, 5]
output = [4, 5, 1, 2, 3]
k=2


def rotate_list(input_list, k):
    k = k%len(input_list)
    return input_list[-k:] + input_list[:-k]
        

print("result - ", rotate_list(input_list, k))
