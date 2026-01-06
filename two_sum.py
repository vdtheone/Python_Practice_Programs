# two sum 
data = [3,6,2,9,5,7]
output = 11

def two_sum_func(data):
    seen = {}
    for index, num in enumerate(data):
        diff = output - num
        if diff in seen:
            print([num, seen[diff]])
            break
        else:
            seen[num] = index

print(two_sum_func(data=data))
