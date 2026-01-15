# Move all zeros to end

# data = [0, 0, 1]
data = [0, 1, 0, 3, 12]
output = [1, 3, 12, 0, 0]


def move_all_zeros_to_end(data):
    non_zeros = []
    zeros = []

    for i in data:
        if i==0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    return non_zeros+zeros

print("result - ", move_all_zeros_to_end(data))


# In-place Optimized Version (Interview Plus)
def move_all_zeros_to_end(data):
    pos = 0
    for num in data:
        if num != 0:
            data[pos] = num
            pos += 1

    for i in range(pos, len(data)):
        data[i] = 0

    return data

print("result - ", move_all_zeros_to_end(data))
