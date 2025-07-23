# 📚 Python Program to Stack Implementation Using OOP


'''
  A stack is a data structure that follows the Last In, First Out (LIFO)
  principle. Elements can be added (pushed) and removed (popped) from the
  top of the stack. In this implementation, we use a class to encapsulate the stack operations.
'''

class Stack:
    def __init__(self):
        self.items = []  # Internal list to store stack elements

    # Method to push an item onto the stack
    # It adds the item to the end of the list 
    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    # Method to pop an item from the stack
    # It removes the last item added to the stackand returns it
    def pop(self):
        # Check if the stack is not empty before popping
        if not self.is_empty():
            # Remove and return the last item added to the stack
            popped = self.items.pop()
            print(f"Popped: {popped}")
            return popped
        # If the stack is empty, print a message and return None
        else:
            print("Stack is empty")
            return None

    # Method to peek at the top item of the stack without removing it
    # It returns the last item added to the stack
    def peek(self):
        # If the stack is not empty, return the last item added to the stack
        if not self.is_empty():
            return self.items[-1]
        # If the stack is empty, return None
        return None

    # Method to check if the stack is empty
    # It returns True if the stack has no items, otherwise False
    def is_empty(self):
        return len(self.items) == 0

    # Method to display the current items in the stack
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
