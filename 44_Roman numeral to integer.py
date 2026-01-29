# Roman numeral to integer
"""
Roman Numeral to Integer
Problem Statement

Given a Roman numeral string, convert it into its corresponding integer value.

Roman numerals are represented by the following symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Special cases use subtraction:

IV = 4

IX = 9

XL = 40

XC = 90

CD = 400

CM = 900

Input 1
s = "III"

Output 1
3

Input 2
s = "LVIII"

Output 2
58

Input 3
s = "MCMXCIV"

Output 3
1994

"""

mapper = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def roman_to_integer(num):
    total = 0
    n = len(num)

    for i in range(n):
        if i < n-1 and mapper[num[i]] < mapper[num[i+1]]:
            total-=mapper[num[i]]
        else:
            total+=mapper[num[i]]
    return total

print("Result = ", roman_to_integer(num="III"))
print("Result = ", roman_to_integer(num="LVIII"))
print("Result = ", roman_to_integer(num="MCMXCIV"))
