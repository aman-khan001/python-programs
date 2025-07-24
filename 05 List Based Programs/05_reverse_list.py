# 📚 Python Program to Reverse a List

'''
  This program reverses a list and returns a new list with the elements in reverse order.
'''

def reverse_list(input_list):
    # Initialize an empty list to store the reversed elements
    reversed_list = []
    # Iterate through the input list in reverse order
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    # Return the reversed list
    return reversed_list

# Example usage
input_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(input_list)
print("Original List:", input_list)
print("Reversed List:", reversed_list)

# 🧠 Explanation:
# The function `reverse_list` takes a list as input and returns a new list with the elements in reverse order.
# It initializes an empty list `reversed_list` to store the reversed items.
# The function iterates through the input list in reverse order using a for loop and appends each item to `reversed_list`.
# Finally, it returns the reversed list.