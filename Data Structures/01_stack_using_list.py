# 📘 Program: Stack Implementation Using List
# This program demonstrates how to use a list as a stack with push/pop operations

'''
  A stack is a data structure that follows the Last In, First Out (LIFO) principle.
  Elements can be added (pushed) and removed (popped) from the top of the stack.
  In Python, lists can be used to implement stacks using append() for push and pop() for pop operations.

'''



# Initializing an empty stack
stack = []

# Pushing elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)  # Output: [10, 20, 30]

# Popping elements from the stack
print("Popped:", stack.pop())  # Removes and returns 30
print("Popped:", stack.pop())  # Removes and returns 20
print("Stack after pops:", stack)  # Output: [10]

# 🧠 Explanation:
# append() adds elements to the end (top of stack)
# pop() removes the last element added (LIFO: Last In, First Out)
