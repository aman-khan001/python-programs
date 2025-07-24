# 📚 Python Program to Remove Duplicates from a List

'''  
  This program removes duplicate elements from a list and returns a new list with unique elements.
'''

def remove_duplicates(input_list):
    # Initialize an empty list to store unique elements
    unique_elements = []
    # Iterate through the input list
    for item in input_list:
        # If the item is not already in the unique_elements list, add it
        if item not in unique_elements:
            unique_elements.append(item)
    # Return the list of unique elements
    return unique_elements

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = remove_duplicates(input_list)
print("Original List:", input_list)
print("List after removing duplicates:", unique_list) 

# 🧠 Explanation:
# The function `remove_duplicates` takes a list as input and returns a new list with duplicate elements removed.
# It initializes an empty list `unique_elements` to store the unique items.
# The function iterates through the input list and adds each item to `unique_elements` only if it's not already present.
# Finally, it returns the list of unique elements.