# Count word frequency

input_data = "Python is easy and Python is powerful"
output = {
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}


def count_word_frequency(input_data):
    # input_data = input_data.lower()
    sentance_list = input_data.split()
    counter = {}
    for i in sentance_list:
        counter[i] = counter.get(i, 0) + 1
    

    return counter
print(count_word_frequency(input_data))