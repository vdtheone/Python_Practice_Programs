# First non-repeating character

"""
    Problem Statement:
    You are given a string.
    Write a program to find the first character that does not repeat in the string.
    If no such character exists, return None.
"""
input_str = "swiss"
output = "w"


def non_repeating_char(input_str):
    freq = {}
    for i in input_str:
        freq[i] = freq.get(i,0)+1

    for char in input_str:
        if freq[char] == 1:
            return char
    return None


print("First non-repeating character - ", non_repeating_char(input_str))
