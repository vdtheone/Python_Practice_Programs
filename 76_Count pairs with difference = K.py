# Count pairs with difference = K

def countPairsWithDiffK(arr, k):
    count = 0
    s = set()
    
    for num in arr:
        if num - k in s:
            count += 1
        if num + k in s:
            count += 1
        s.add(num)
    
    return count

# Example usage
arr = [1, 5, 3, 4, 2]
k = 2
result = countPairsWithDiffK(arr, k)
print(result)  # Output: 3 (pairs are (1, 3), (5, 3), (4, 2))