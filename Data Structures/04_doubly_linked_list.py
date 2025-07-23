# 📚 Python Program to Doubly Linked List Implementation

'''
  A doubly linked list is a linear data structure where each node contains a reference to both the next and previous nodes.
'''


# Node class for doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Points to the previous node
        self.next = None  # Points to the next node

# DoublyLinkedList class to manage the list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append a node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Method to display the list forward
    def display_forward(self):
        current = self.head
        print("Forward:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            last = current
            current = current.next
        print("None")

    # Method to display the list backward
    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        print("Backward:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Testing the doubly linked list
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

# Display the list in both directions
dll.display_forward()   # Output: 10 <-> 20 <-> 30 <-> None
dll.display_backward()  # Output: 30 <-> 20 <-> 10 <-> None

# 🧠 Explanation:
# Each node has two pointers: one to the next node and one to the previous node.
# This allows bidirectional traversal of the list.
