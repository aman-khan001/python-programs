# 📘 Program: Queue Implementation Using OOP
# This program demonstrates how to implement a queue using a class



class Queue:
    def __init__(self):
        self.items = []  # Internal list to store queue elements

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

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
