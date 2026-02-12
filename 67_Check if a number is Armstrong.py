# Check if a number is Armstrong

num = 153

def check_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return sum_of_powers == num 

print(check_armstrong_number(num))
