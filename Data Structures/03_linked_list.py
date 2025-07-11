# 📘 Program: Singly Linked List Implementation
# This program demonstrates the creation and traversal of a singly linked list

'''
  A singly linked list is a linear data structure where each element (node) points to the next node.
'''

# Node class to represent each element of the list
class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Pointer to the next node

# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Method to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # First node becomes head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Add at the end

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating and testing the linked list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("Linked List:")
ll.display()  # Output: 10 -> 20 -> 30 -> None

# 🧠 Explanation:
# Each node contains data and a reference to the next node.
# LinkedList manages the nodes and supports adding and traversing.
