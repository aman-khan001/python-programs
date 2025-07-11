# 📘 Program: Bubble Sort Algorithm
# This program demonstrates how to sort a list using bubble sort

'''
  Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
  compares adjacent elements and swaps them if they are in the wrong order.
  The pass through the list is repeated until no swaps are needed, which means the list is sorted.
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):  
        # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Unsorted list
data = [64, 25, 12, 22, 11]
print("Original list:", data)

# Sorting the list
bubble_sort(data)
print("Sorted list:", data)

# 🧠 Explanation:
# Bubble sort compares adjacent elements and swaps them if they are in wrong order.
# Time complexity is O(n^2) in worst case, best for small datasets or learning.
