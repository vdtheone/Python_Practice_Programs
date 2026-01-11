# Find largest and smallest in a list

data = [2,4,6,1,8,50,46,34]

largest = float("-inf")
smallest = float("+inf")

for i in data:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("largest - ", largest)
print("smallest - ", smallest)