# Find missing number (1–N)

data = [1, 2, 4, 5, 6]
output = 3

n = len(data) + 1
sum_of_max_num = n*(n+1)//2

print('missing Num : ', sum_of_max_num - sum(data))