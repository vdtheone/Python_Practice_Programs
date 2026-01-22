# Top K frequent elements
"""
Top K Frequent Elements

Problem Statement:
Given a list of elements and an integer k, return the k most frequent elements.

Input:

nums = [1, 1, 1, 2, 2, 3]
k = 2


Output:

[1, 2]


Input:

nums = ["apple", "banana", "apple", "orange", "banana", "apple"]
k = 1


Output:

["apple"]
"""

nums_1 = [1, 1, 1, 2, 2, 3]
k_1 = 2

nums_2 = ["apple", "banana", "apple", "orange", "banana", "apple"]
k_2 = 1

def top_k_frequent_element(nums, k):
    freq = {}

    for i in nums:
        freq[i] = freq.get(i,0)+1

    sorted_items = sorted(freq.items(), key=lambda item:item[1], reverse=True)
    return [i[0] for i in sorted_items[:k]]

print("Result - ", top_k_frequent_element(nums_1, k_1))
print("Result - ", top_k_frequent_element(nums_2, k_2))
