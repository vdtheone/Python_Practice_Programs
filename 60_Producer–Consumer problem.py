# Producer–Consumer problem

"""

Implement the Producer-Consumer problem using Python.

    A Producer produces items and puts them into a shared buffer.
    A Consumer consumes items from the buffer.
    The buffer has a fixed size.
    The producer must wait if the buffer is full.
    The consumer must wait if the buffer is empty.

You must ensure:

    Thread safety
    No race conditions
    Proper synchronization

Requirements
    Use Python threading
    Use a shared buffer (queue or list)
    Use synchronization primitives (Lock / Semaphore / Condition)

"""

# import threading
# import time
# import random

# buffer = []
# BUFFER_SIZE = 5

# condition = threading.Condition()

# def producer():
#     for i in range(10):
#         item = random.randint(1, 100)

#         with condition:
#             while len(buffer) == BUFFER_SIZE:
#                 print("Buffer full → Producer waiting")
#                 condition.wait()

#             buffer.append(item)
#             print(f"Produced: {item} | Buffer: {buffer}")

#             condition.notify()  # wake up consumer

#         time.sleep(1)

# def consumer():
#     for i in range(10):
#         with condition:
#             while not buffer:
#                 print("Buffer empty → Consumer waiting")
#                 condition.wait()

#             item = buffer.pop(0)
#             print(f"Consumed: {item} | Buffer: {buffer}")

#             condition.notify()  # wake up producer

#         time.sleep(2)

# producer_thread = threading.Thread(target=producer)
# consumer_thread = threading.Thread(target=consumer)

# producer_thread.start()
# consumer_thread.start()

# producer_thread.join()
# consumer_thread.join()



import threading
import time
import random
from queue import Queue

buffer = Queue(maxsize=5)

def producer():
    for i in range(10):
        item = random.randint(1, 100)

        buffer.put(item)  # blocks if buffer is full
        print(f"Produced: {item} | Size: {buffer.qsize()}")

        time.sleep(1)

def consumer():
    for i in range(10):
        item = buffer.get()  # blocks if buffer is empty
        print(f"Consumed: {item} | Size: {buffer.qsize()}")

        buffer.task_done()
        time.sleep(2)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

