# Check if string follows a pattern

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for c, word in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != word:
                return False
        else:
            char_to_word[c] = word

        if word in word_to_char:
            if word_to_char[word] != c:
                return False
        else:
            word_to_char[word] = c

    return True

# Example usage:
pattern = "abba"
s = "dog cat cat dog"
print("Result:", wordPattern(pattern, s))  # Output: True

pattern = "abba"
s = "dog cat cat fish"
print("Result:", wordPattern(pattern, s))  # Output: False

pattern = "aaaa"
s = "dog cat cat dog"
print("Result:", wordPattern(pattern, s))  # Output: False

pattern = "abba"
s = "dog dog dog dog"
print("Result:", wordPattern(pattern, s))  # Output: False

