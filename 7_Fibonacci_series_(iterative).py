# Fibonacci series (iterative)

input_number = int(input("enter a number - "))

def fibonacci_series(num):
    a,b = 0,1
    for i in range(num):
        print(a)
        next_number = a+b
        a = b
        b = next_number

        # second approach
        # a, b = b, a + b

fibonacci_series(input_number)
