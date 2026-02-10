# Small utility module

from utils import (
    is_palindrome,
    flatten_list,
    safe_divide,
    count_words
)

print(is_palindrome("A man a plan a canal Panama"))

print(flatten_list([1, [2, [3, 4]]]))

try:
    print(safe_divide(10, 0))
except Exception as e:
    print("Error:", e)

print(count_words("Python is easy and Python is powerful"))
