# Count vowels, consonants, digits

input_str = "aB3dE9xY0"

vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels = 0
consonants = 0
digits = 0

for i in input_str:
    if i.isdigit():
        digits+=1
    elif i.isalpha() and i in vowels_list:
        vowels+=1
    else:
        consonants+=1

print("vowels, consonants, digits = ", vowels, consonants, digits)



