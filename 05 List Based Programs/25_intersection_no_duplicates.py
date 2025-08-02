# 📚 Python Program to Find Intersection of Two Lists Without Duplicates

'''
  This program finds the intersection of two lists and returns a new list containing only unique elements.
'''

def intersection_no_duplicates(list1, list2):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    # Find the intersection of both sets
    intersection = set1.intersection(set2)
    # Convert the result back to a list
    return list(intersection)

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection_no_duplicates(list1, list2)
print("Intersection without duplicates:", result)

# 🧠 Explanation:
# The function intersection_no_duplicates takes two lists as input.
# It converts both lists to sets to eliminate any duplicates.
# Then, it finds the intersection of these sets using the intersection method.
# Finally, it converts the intersection back to a list and returns it.