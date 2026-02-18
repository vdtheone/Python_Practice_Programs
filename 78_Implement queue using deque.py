# Implement queue using deque

from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception("Queue underflow: Cannot dequeue item, queue is empty.")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("Queue is empty: Cannot peek item.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())  # Output: 1
    print(queue.dequeue())   # Output: 1
    print(queue.size())  # Output: 2
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()  # This will raise an exception since the queue is empty.