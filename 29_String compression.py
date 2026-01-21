# String compression

"""
Problem Statement:
Given a string, compress it by replacing consecutive repeating characters with the character followed by the count.
If the compressed string is not shorter than the original string, return the original string.

Input:
"aabcccccaaa"


Output:
"a2b1c5a3"
"""

input_str_1 = "aabcccccaaa"
input_str_2 = "abc"
input_str_3 = "aaabb"


def compression_str(input_str):
    new_str = ""
    count = 1
    for i in range(0, len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            count+=1
        else:
            new_str+=input_str[i]+str(count)
            count = 1
    new_str=new_str+input_str[-1]+str(count)
    
    return new_str if len(new_str) < len(input_str) else input_str


print("result - ", compression_str(input_str_1))
print("result - ", compression_str(input_str_2))
print("result - ", compression_str(input_str_3))

