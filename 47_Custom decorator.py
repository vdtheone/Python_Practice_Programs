# Custom decorator

"""
Create a custom decorator called my_decorator that:

Prints "Function started" before the function executes

Prints "Function ended" after the function executes

Input
@my_decorator
def greet():
    print("Hello World")

Expected Output

Function started
Hello World
Function ended

"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args)
        print("Function ended")
        return result
    return wrapper


@my_decorator
def greet():
    print("Hello World")

greet()
