# Generate subsets

"""
Given a list of unique elements, generate all possible subsets (the power set).

A subset may be empty and does not require continuity.

🔹 Input 1
nums = [1, 2, 3]

🔹 Output 1
[
  [],
  [1],
  [2],
  [3],
  [1, 2],
  [1, 3],
  [2, 3],
  [1, 2, 3]
]

🔹 Input 2
nums = ["a", "b"]

🔹 Output 2
[
  [],
  ["a"],
  ["b"],
  ["a", "b"]
]

🔹 Input 3
nums = [1]

🔹 Output 3
[
  [],
  [1]
]

"""

input_data_1 = [1, 2, 3]
input_data_2 = ["a", "b"]
input_data_3 = [1]


def generate_subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        # Exclude
        backtrack(index + 1, current)

        # Include
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()

    backtrack(0, [])
    return result

print("result = ", generate_subsets(input_data_1))
print("result = ", generate_subsets(input_data_2))
print("result = ", generate_subsets(input_data_3))
