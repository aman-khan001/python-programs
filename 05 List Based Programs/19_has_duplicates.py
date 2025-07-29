# 📚 Python Program to Check for Duplicates in a List

'''  
  This program checks if a list contains any duplicate elements.
'''

def has_duplicates(lst):
    return len(lst) != len(set(lst))

# Example usage
my_list = [1, 2, 3, 4, 5, 1]
if has_duplicates(my_list):
    print("The list has duplicates.")
else:
    print("The list has no duplicates.")

# 🧠 Explanation:
# The function has_duplicates checks if the list contains any duplicate elements.
# It does this by comparing the length of the original list with the length of the set created from the list.
# Since sets do not allow duplicate values, if the lengths are different, duplicates exist.