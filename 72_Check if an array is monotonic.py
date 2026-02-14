# Check if an array is monotonic

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 


def isMonotonic(A):
    increasing = decreasing = True
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            decreasing = False
        if A[i] < A[i - 1]:
            increasing = False
    return increasing or decreasing

print(isMonotonic([1, 2, 3, 4, 5]))
print(isMonotonic([5, 4, 3, 2, 1]))
print(isMonotonic([1, 2, 2, 3]))
print(isMonotonic([1, 3, 2]))   