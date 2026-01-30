# Prime number check

def check_prime(num):
    if num <= 1:
        print(f"{num} is not Prime")
        return  
    
    for i in range(2,num):
        if num%i==0:
            return False
    return True

input_number = int(input("enter a number - "))
if check_prime(input_number):
    print(f"{input_number} is Prime")
else:
    print(f"{input_number} is Not Prime")

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, n))

print(f"{input_number} is Prime" if is_prime(input_number) else f"{input_number} is Not Prime")