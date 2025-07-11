# 📘 Program: Stack Implementation Using OOP
# This program demonstrates how to implement a stack using a class

class Stack:
    def __init__(self):
        self.items = []  # Internal list to store stack elements

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            popped = self.items.pop()
            print(f"Popped: {popped}")
            return popped
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", self.items)

# Using the Stack class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()

# 🧠 Explanation:
# Stack follows LIFO (Last In, First Out).
# We use a list to store elements and provide methods for common stack operations.
