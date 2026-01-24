# Sum of digits (recursive)

nums = [2,3,1,6,8,9,10]
nums = [1,2,3,4,5]


def sum_of_digits(nums):
    total = 0
    for i in nums:
        total+=i
    return total

print("result = ", sum_of_digits(nums))


# Using nums[1:] creates a new list each time.
def sum_of_digits(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_of_digits(nums[1:])

print("result = ", sum_of_digits(nums))


def sum_of_digits(nums, i=0):
    if i == len(nums):
        return 0
    return nums[i] + sum_of_digits(nums, i+1)

print("result = ", sum_of_digits(nums))
