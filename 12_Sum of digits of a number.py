# Sum of digits of a number

input_number = int(input("enter a number - "))

def Sum_of_digits(input_number):
    new_num = 0
    while input_number!=0:
        rem = input_number%10
        new_num+=rem
        input_number = input_number//10
    return new_num

print("Sum of digits = ",Sum_of_digits(input_number))
