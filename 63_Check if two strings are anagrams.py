# Check if two strings are anagrams

str1 = "listen"
str2 = "silent"

def check_anagrams_strings(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1==sorted_str2

print(check_anagrams_strings(str1, str2))
