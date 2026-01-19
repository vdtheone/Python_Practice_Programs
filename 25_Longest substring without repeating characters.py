# Longest substring without repeating characters

input_str = "abcabcbb"
output = 3

def longest_substr(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
    

print("result = ", longest_substr(input_str))