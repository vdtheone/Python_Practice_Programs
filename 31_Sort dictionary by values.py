# Sort dictionary by values
"""
Problem Statement:
Given a dictionary, sort it by its values in ascending order.

Input:

{"a": 3, "b": 1, "c": 2}


Output:

{"b": 1, "c": 2, "a": 3}


Input:

{"apple": 10, "banana": 5, "orange": 8}


Output:

{"banana": 5, "orange": 8, "apple": 10}
"""

input_dict_1 = {"a": 3, "b": 1, "c": 2}
input_dict_2 = {"apple": 10, "banana": 5, "orange": 8}


def sort_dict_values(input_dict:dict):
    return dict(sorted(input_dict.items(), key=lambda item:item[1]))


print("Result - ", sort_dict_values(input_dict_1))
print("Result - ", sort_dict_values(input_dict_2))
