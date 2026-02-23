# Insert and delete nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if not current_node:
            raise IndexError("Position out of bounds")
        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, position):
        if not self.head:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if not current_node or not current_node.next:
            raise IndexError("Position out of bounds")
        current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.insert(2, 1)  # Insert 2 at position 1
linked_list.print_list()  # Output: 1 2 3
linked_list.delete(1)  # Delete node at position 1
linked_list.print_list()  # Output: 1 3
