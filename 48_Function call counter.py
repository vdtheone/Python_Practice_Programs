# Function call counter
"""
Function Call Counter (Decorator)
📌 Problem Statement

Create a decorator called count_calls that:

Counts how many times a function is called

Prints the function name and call count every time it is invoked

Input
@count_calls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

Expected Output
say_hello has been called 1 times
Hello
say_hello has been called 2 times
Hello
say_hello has been called 3 times
Hello

🧩 Problem 3: Function Call Counter (Multiple Functions)
📌 Problem Statement

Enhance the count_calls decorator so that:

Each function maintains its own call count

Call counts do not mix between functions

Input
@count_calls
def add(a, b):
    return a + b

@count_calls
def multiply(a, b):
    return a * b

add(2, 3)
add(4, 5)
multiply(2, 3)
multiply(4, 5)

Expected Output
add has been called 1 times
add has been called 2 times
multiply has been called 1 times
multiply has been called 2 times

🧩 Problem 4: Decorator With Arguments (Advanced)
📌 Problem Statement

Create a decorator repeat(n) that:

Executes the decorated function n times

Prints the result each time

Input
@repeat(3)
def say_hi():
    print("Hi")

Expected Output
Hi
Hi
Hi

"""
from functools import wraps

def count_calls(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()


@count_calls
def add(a, b):
    return a + b

@count_calls
def multiply(a, b):
    return a * b

add(2, 3)
add(4, 5)
multiply(2, 3)
multiply(4, 5)



def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi")

say_hi()