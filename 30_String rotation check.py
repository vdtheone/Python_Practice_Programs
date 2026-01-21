# String rotation check

"""
Problem Statement:
Given two strings s1 and s2, check if s2 is a rotation of s1.
A string is a rotation if it can be obtained by rotating s1 any number of times.

Input:
s1 = "abcd"
s2 = "cdab"

Output:
True

Input:
s1 = "abcd"
s2 = "acbd"

Output:
False
"""

s1 = "abcd"
s2 = "cdab"

s3 = "abcd"
s4 = "acbd"


def rotation_check(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
    

print("result - ", rotation_check(s1, s2))
print("result - ", rotation_check(s3, s4))
