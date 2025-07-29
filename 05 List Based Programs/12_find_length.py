# 📚 Python Program to Find the Length of a List 

'''
  This program finds the length of a list without using the built-in `len()` function.
'''

def find_length(lst):
    # Initialize a counter to zero
    count = 0
    # Iterate through the list and count each element
    for _ in lst:
        count += 1
    return count

# Example usage
print("Length of the list:", find_length([1, 2, 3, 4, 5]))

# 🧠 Explanation:
# The find_length function takes a list as input and returns its length.
# It initializes a counter to zero, iterates through each element in the list,
# increments the counter for each element, and finally returns the total count.
