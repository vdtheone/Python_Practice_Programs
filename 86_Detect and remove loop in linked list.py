# Detect and remove loop in linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def detect_and_remove_loop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    fast.next = None
    return head


# Example usage
linked_list = LinkedList()
linked_list.append(1)   
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
# Create a loop for testing
linked_list.tail.next = linked_list.head.next.next  # Connect tail to node with value 3
head = detect_and_remove_loop(linked_list.head)
current = head
while current:
    print(current.value)
    current = current.next