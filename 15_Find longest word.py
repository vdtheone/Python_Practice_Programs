# Find longest word

input_data = "Python makes backend development powerful"
output = "development"


def find_longest_word(input_data):
    words = input_data.split()
    longest_word = words[0]
    for word in words:
        if len(word)>len(longest_word):
            longest_word = word
    return longest_word
    

print(find_longest_word(input_data))