# Parameterized Decorator in Python

def add_c(c):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result = result + c
            return result
        return wrapper
    return decorator


@add_c(3)
def add_num(a, b):
    return a + b

print("result = ", add_num(1, 2))