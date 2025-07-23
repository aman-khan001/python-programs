# 📚 Python Program to Queue Implementation Using OOP


'''
  A queue is a linear data structure that follows the First In First Out (FIFO)
  principle. Elements are added to the end of the queue (enqueue) and removed from the
  front (dequeue). In this implementation, we use a class to encapsulate the queue
  operations.
'''


class Queue:
    def __init__(self):
        self.items = []  # Internal list to store queue elements

    # Method to enqueue an item to the queue
    # It adds the item to the end of the list
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    # Method to dequeue an item from the queue
    # It removes the first item added to the queue and returns it
    def dequeue(self):
        if not self.is_empty():
            # Remove and return the first item added to the queue
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            # Return the removed item
            return removed
        # If the queue is empty, print a message and return None
        else:
            print("Queue is empty")
            return None

    # Method to peek at the front item of the queue without removing it
    # It returns the first item added to the queue
    def peek(self):
        if not self.is_empty():
            # Return the first item in the queue
            return self.items[0]
        return None

    # Method to check if the queue is empty
    # It returns True if the queue has no items, otherwise False
    def is_empty(self):
        return len(self.items) == 0

    # Method to display the current items in the queue
    def display(self):
        print("Queue:", self.items)

# Using the Queue class
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.display()
queue.dequeue()
queue.display()

# 🧠 Explanation:
# Queue follows FIFO (First In, First Out).
# Elements are added to the end and removed from the front.
