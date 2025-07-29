# 📚 Python Program to Sort Elements in Ascending Order

'''  
  This program sorts a list of numbers in ascending order using a simple sorting algorithm. 
  It implements a basic bubble sort-like approach to rearrange the elements in ascending order without using the built-in sort() function

'''

def sort_elements_ascending(arr):
    # Iterate through the list and compare each element with the others
    for i in range(len(arr)):
        # Compare the current element with the rest of the elements
        for j in range(i + 1, len(arr)):
            # If the current element is greater than the next element, swap them
            if arr[i] > arr[j]:
                # Swap the elements to arrange them in ascending order
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Example usage
data = [64, 25, 12, 22, 11]
print("Original list:", data)
sorted_data = sort_elements_ascending(data)
print("Sorted list:", sorted_data)

# 🧠 Explanation:
# The function sort_elements_ascending takes a list as input and sorts it in ascending order.
# It uses a nested loop to compare each element with the others and swaps them if they are in the wrong order.
# This process continues until the entire list is sorted.