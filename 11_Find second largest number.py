# Find second largest number

numbers = [2,4,6,3,5]

first, second = float("-inf"), float("-inf")

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num < first and num > second:
        second = num

print("second_largest - ", second)