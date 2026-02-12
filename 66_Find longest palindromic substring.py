# Find longest palindromic substring

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
                print('longest: ', longest)
    return longest

# Example usage
input_string = "babad"
result = longest_palindrome(input_string)
print("Longest palindromic substring:", result) 