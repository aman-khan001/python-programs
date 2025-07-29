# 📚 Python Program to Find Duplicates in a List

'''
  This program finds all duplicate elements in a list.
'''

def find_duplicates(lst):
    # Initialize a set to keep track of seen elements and another set for duplicates
    seen = set()
    duplicates = set()
    
    # Iterate through the list
    for item in lst:
        if item in seen:
            # If the item is already seen, add it to duplicates
            duplicates.add(item)
        else:
            # If the item is not seen, add it to seen
            seen.add(item)
    
    return list(duplicates)

# Example usage
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 1]
print("Duplicates in the list are:", find_duplicates(my_list))

# 🧠 Explanation:
# The function find_duplicates takes a list as input and returns a list of duplicate elements.
# It uses two sets: 'seen' to keep track of all unique elements and 'duplicates' to keep track of all duplicate elements.
# As it iterates through the list, it checks if an element is in the 'seen' set.
# If it is, the element is added to the 'duplicates' set.
# If it isn't, the element is added to the 'seen' set.
# Finally, the function returns the 'duplicates' set as a list.
