# Queue using two stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out


# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1 
print(queue.peek())     # Output: 2
print(queue.dequeue())  # Output: 2
print(queue.is_empty()) # Output: True
queue.enqueue(3)
print(queue.peek())     # Output: 3
print(queue.dequeue())  # Output: 3
print(queue.is_empty()) # Output: True