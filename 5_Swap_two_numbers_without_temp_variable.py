# Swap two numbers without temp variable

a = 10
b = 20

def swap_num(a, b):
    # a,b = b,a
    a = a+b
    b = a-b
    a = a-b
    return a, b

a, b = swap_num(a,b)

print("a - ", a)
print("b - ", b)