# two sum 
data = [2, 7, 11, 15]
target = 9

def two_sum_func(data):
    seen = {}
    for index, num in enumerate(data):
        diff = target - num
        if diff in seen:
            print([seen[diff], index])
            break
        else:
            seen[num] = index

print(two_sum_func(data=data))
