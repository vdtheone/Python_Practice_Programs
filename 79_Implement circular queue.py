# Implement circular queue

def circular_queue(n):
    queue = [None] * n
    head = 0
    tail = 0
    size = 0

    def enqueue(value):
        nonlocal tail, size
        if size == n:
            raise Exception("Queue is full")
        queue[tail] = value
        tail = (tail + 1) % n
        size += 1

    def dequeue():
        nonlocal head, size
        if size == 0:
            raise Exception("Queue is empty")
        value = queue[head]
        head = (head + 1) % n
        size -= 1
        return value

    def front():
        if size == 0:
            raise Exception("Queue is empty")
        return queue[head]

    def rear():
        if size == 0:
            raise Exception("Queue is empty")
        return queue[(tail - 1 + n) % n]

    return enqueue, dequeue, front, rear


# Example usage
enqueue, dequeue, front, rear = circular_queue(5)
enqueue(1)
enqueue(2)
enqueue(3)
print("Front:", front())  # Output: Front: 1
print("Rear:", rear())    # Output: Rear: 3
dequeue()
print("Front after dequeue:", front())  # Output: Front after dequeue: 2
enqueue(4)
enqueue(5)
print("Rear after enqueue 4 and 5:", rear())  # Output: Rear after enqueue 4 and 5: 5
enqueue(6)  # This will raise an exception because the queue is full  