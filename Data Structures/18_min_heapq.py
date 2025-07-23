# 📚 Python Program to Min Heap Using heapq in Python


'''
   A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children.
'''

import heapq

# Creating an empty min heap
min_heap = []

# Adding elements to the heap (in any order)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 30)

print("Heap after pushes:", min_heap)  # The smallest element is always at index 0

# Removing the smallest element
print("Popped element:", heapq.heappop(min_heap))
print("Heap after pop:", min_heap)

# Accessing the smallest element without removing it
print("Peek (min element):", min_heap[0])

# 🧠 Explanation:
# heapq creates a min-heap by default.
# heappush adds an element and maintains heap order.
# heappop removes the smallest element.
# Time complexity: O(log n) for push/pop, O(1) for peek.
