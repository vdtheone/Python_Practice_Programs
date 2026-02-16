# Find longest increasing subsequence (basic)

def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n  # Initialize the dp array with 1s
    print('dp: ', dp)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if we can extend the subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The length of the longest increasing subsequence

# Example usage
arr = [10, 20, 10, 30, 20, 50]
length = longest_increasing_subsequence(arr)
print(length)  # Output: 4 (the longest increasing subsequence is [10, 20, 30, 50])