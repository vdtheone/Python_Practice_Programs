# Factorial (iterative & recursive)

num = 5

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i

    return fact

print("Result = ", factorial(num))


def fact_rec(num):
    if num<=1:
        return 1
    return num * fact_rec(num-1)

print("Result = ", fact_rec(num))
