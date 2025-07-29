# 📚 Python Program to Check if Two Lists are Identical

'''
  This program checks if two lists are identical, meaning they have the same elements in the same order.
'''

def are_identical(list1, list2):
    # Check if the lengths of the lists are the same
    if len(list1) != len(list2):
        return False
    # Check each element for equality
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# Example usage
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
print("Are list_a and list_b identical?", are_identical(list_a, list_b))
print("Are list_a and list_c identical?", are_identical(list_a, list_c))

# 🧠 Explanation:
# The are_identical function takes two lists as input and checks if they are identical.
# It first compares their lengths, and if they are not the same, it returns False.
# If the lengths are the same, it iterates through the elements and compares them one by one.
# If all elements are equal, it returns True; otherwise, it returns False.
