"""Reverse a list using recursion.

This module exposes `reverse_list_recursive(nums)` which returns a new list
containing the elements of `nums` in reverse order. The implementation is
recursive and returns a fresh list (does not mutate the input).
"""

from typing import List


def reverse_list_recursive(nums: List[int]) -> List[int]:
    """Return a new list that is the reverse of `nums` using recursion.

    Examples:
        >>> reverse_list_recursive([1, 2, 3])
        [3, 2, 1]
    """
    if not nums:
        return []
    if len(nums) == 1:
        return nums[:]  # return a shallow copy for consistency

    return [nums[-1]] + reverse_list_recursive(nums[:-1])


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print("result =", reverse_list_recursive(sample))