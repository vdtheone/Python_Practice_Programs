# Infinite Fibonacci generator

def fibonacci_generator():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci_generator()

print(next(gen))
print(next(gen))
print(next(gen))

print("=======================")

for _ in range(4):
    print(next(gen))