# Merge two sorted linked lists

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
        
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next


# Example usage
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
merged_list = merge_sorted_lists(list1.head, list2.head)
while merged_list:
    print(merged_list.value)
    merged_list = merged_list.next
# Output: 1 2 3 4 5 6