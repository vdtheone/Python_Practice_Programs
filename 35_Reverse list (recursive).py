# Reverse list (recursive)

nums = [1,2,3,4,5]

def reverse_list_recursive(nums):
    if len(nums) == 0:
        return []
    
    # Recursive case
    return [nums[-1]] + reverse_list_recursive(nums[:-1])


print("result = ", reverse_list_recursive(nums))