# Reverse a string (no slicing)

input_str = "abcd"
output = "dcba"

result = ""

for i in input_str:
    result = i+result

print("result = ", result)