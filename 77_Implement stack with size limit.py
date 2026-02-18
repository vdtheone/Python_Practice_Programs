# Implement stack with size limit

class Stack:
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            raise Exception("Stack overflow: Cannot push item, stack is full.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack underflow: Cannot pop item, stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty: Cannot peek item.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
if __name__ == "__main__":
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # Output: 3
    print(stack.pop())   # Output: 3
    print(stack.size())  # Output: 2
    stack.push(4)       # This will raise an exception since the stack is full.