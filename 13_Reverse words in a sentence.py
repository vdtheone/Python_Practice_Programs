# Reverse words in a sentence

input_sentence = "Python is easy to learn"
output = "learn to easy is Python"


def reverse_word_sentence(input_sentence):
    sentence_list = input_sentence.split()
    return " ".join(sentence_list[::-1])

print(reverse_word_sentence(input_sentence))