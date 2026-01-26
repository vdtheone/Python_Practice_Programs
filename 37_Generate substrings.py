# Generate substrings
"""
Given a string, generate all possible substrings of the string.

A substring is a continuous sequence of characters taken from the string.

Input 1
s = "abc"

Output 1
["a", "ab", "abc", "b", "bc", "c"]

🔹 Input 2
s = "aa"

Output 2
["a", "aa", "a"]


✔ Order doesn’t matter unless specified
✔ Duplicates allowed

Input 3
s = "abcd"

🔹 Output 3
["a", "ab", "abc", "abcd",
 "b", "bc", "bcd",
 "c", "cd",
 "d"]

"""

input_str_1 = "abc"
input_str_2 = "aa"
input_str_3 = "abcd"


def generate_substr(input_str):
    data = []
    n = len(input_str)
    for i in range(n):
        for j in range(i+1, n+1):
            data.append(input_str[i:j])
    return data
    
print("Result = ", generate_substr(input_str_1))
print("Result = ", generate_substr(input_str_2))
print("Result = ", generate_substr(input_str_3))