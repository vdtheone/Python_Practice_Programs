# Permutations of string

"""
Given a string containing unique characters, generate all possible permutations of the string.

A permutation is a rearrangement of all characters in the string such that each arrangement is unique.

Input 1
s = "abc"

Output 1
["abc", "acb", "bac", "bca", "cab", "cba"]

Input 2
s = "ab"

Output 2
["ab", "ba"]

Input 3
s = "a"

Output 3
["a"]
"""

input_str_1 = "abc"

def permutation_of_string(input_str:str):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            backtrack(
                path + remaining[i],
                remaining[:i] + remaining[i+1:]
            )

    backtrack(path="", remaining=input_str)
    return result


print("Result = ", permutation_of_string(input_str_1))