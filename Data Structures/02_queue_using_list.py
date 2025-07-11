# 📘 Program: Queue Implementation Using List
# This program demonstrates how to use a list as a queue with enqueue/dequeue operations

'''
  A queue is a linear data structure that follows the First In First Out (FIFO) principle.
'''


# Initializing an empty queue
queue = []

# Enqueuing elements to the queue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueues:", queue)  # Output: ['A', 'B', 'C']

# Dequeuing elements from the queue
print("Dequeued:", queue.pop(0))  # Removes and returns 'A'
print("Dequeued:", queue.pop(0))  # Removes and returns 'B'
print("Queue after dequeues:", queue)  # Output: ['C']

# 🧠 Explanation:
# append() adds elements to the end of the list
# pop(0) removes elements from the front (FIFO: First In, First Out)
# 📝 Note:
# Using a list as a queue is simple but not the most efficient for large queues
# as pop(0) has O(n) time complexity.
# For better performance with large queues, consider using collections.deque

