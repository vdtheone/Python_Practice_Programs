# Stack using list

"""Implement a stack using a list that supports push, pop, peek, and is_empty operations."""

# Input / Operations:
"""
    push(10)
    push(20)
    push(30)
    pop()
    peek()
    is_empty()
"""

def push(stack, num):
    stack.append(num)

def pop_num(stack):
    if not stack:
        return "Stack is empty"
    return stack.pop()

def print_list(stack):
    print(stack)

def peek_num(stack:list):
    if not stack:
        return "Stack is empty"
    return stack[-1]

def is_empty(stack):
    return len(stack) == 0

def stack_list():
    stack = []

    while True:
        print("\n1 - Push")
        print("2 - Pop")
        print("3 - Peek")
        print("4 - Print")
        print("5 - Is Empty")
        print("6 - Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            num = int(input("Enter number: "))
            push(stack, num)

        elif choice == 2:
            print(pop_num(stack))

        elif choice == 3:
            print(peek_num(stack))

        elif choice == 4:
            print_list(stack)

        elif choice == 5:
            print(is_empty(stack))

        elif choice == 6:
            break
        
stack_list()


# Class Based

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)
#         print(f"{value} pushed to stack")

#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack.pop()

#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack[-1]

#     def is_empty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)

#     def display(self):
#         print("Stack:", self.stack)


# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# print("Pop:", s.pop())
# print("Peek:", s.peek())
# print("Is Empty:", s.is_empty())
# print("Size:", s.size())
# s.display()
