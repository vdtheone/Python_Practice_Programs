# Power function without **

"""
Implement a function to calculate x raised to the power n (xⁿ) without using the built-in power operator (**) or pow().

Input 1
x = 2
n = 3

Output 1
8

Input 2
x = 5
n = 0

Output 2
1

Input 3
x = 2
n = -2

Output 3
0.25

"""

def power_function(x, n):
    if n == 0:
        return 1
    
    result = 1
    power = abs(n)
    
    for _ in range(power):
        result*=x

    return result if n > 0 else 1 / result

print("Result = ", power_function(2, 3))
print("Result = ", power_function(5, 0))
print("Result = ", power_function(2, -2))


def power_function_fast(x, n):
    if n == 0:
        return 1

    half = power_function_fast(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half if n > 0 else (half * half) / x

print("power_function_fast Result = ", power_function_fast(2, 3))