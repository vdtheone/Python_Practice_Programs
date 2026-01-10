# Check palindrome (string and number)

# for number

input_data = int(input("enter a number  - "))

def check_pallindrom_num(num):
    original_num = num
    reverse_num = 0

    while(num!=0):
        rem = num%10
        reverse_num = reverse_num*10+rem
        num = num//10
    return original_num == reverse_num

print("Number is Pallindrom - ", check_pallindrom_num(num=input_data))


# for String

string_input = input("enter string input - ")
def check_pallindrom_str(string_input):
    if string_input == string_input[::-1]:
        return True
    else:
        return False

print("String is Pallindrom = ", check_pallindrom_str(string_input))
