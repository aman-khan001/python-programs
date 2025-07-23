# 📘 Program: Max Heap Using heapq in Python


'''
    A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children.
'''

import heapq

# Python's heapq module implements a min-heap, so to simulate a max-heap,
# we store negative values and invert them when accessing

max_heap = []

# Adding elements to the max heap
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -30)

print("Heap after pushes (as negatives):", max_heap)

# Converting back to positive to show as max heap
print("Max Heap (actual values):", [-x for x in max_heap])

# Removing the largest element (which is the smallest negative number)
print("Popped max element:", -heapq.heappop(max_heap))
print("Heap after pop (actual values):", [-x for x in max_heap])

# Peek the max element
print("Peek (max element):", -max_heap[0])

# 🧠 Explanation:
# Max Heap is simulated by pushing negative values in heapq.
# When retrieving values, we convert them back to positive.
# This lets us use heapq as a max heap efficiently.