# 📚 Python Program to Set Operations in Python


'''
  A set is an unordered collection of unique elements. 
  It supports mathematical set operations like union, intersection, difference, and symmetric difference.
  Sets are useful for membership testing and eliminating duplicate entries.
  They are implemented using hash tables, which allows for efficient operations.
  Common operations include adding, removing elements, and checking membership.
'''


# Creating two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of sets
print("Union:", set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
print("Intersection:", set_a & set_b)  # Output: {4, 5}

# Difference of sets
print("A - B:", set_a - set_b)  # Output: {1, 2, 3}
print("B - A:", set_b - set_a)  # Output: {8, 6, 7}

# Symmetric Difference (elements in A or B but not both)
print("Symmetric Difference:", set_a ^ set_b)  # Output: {1, 2, 3, 6, 7, 8}

# Checking membership
print("Is 3 in Set A?", 3 in set_a)  # Output: True
print("Is 6 in Set A?", 6 in set_a)  # Output: False

# Iterating through a set
for element in set_a:
    print("Element in Set A:", element)


# Adding and removing elements
set_a.add(10)
set_a.discard(2)
print("Modified Set A:", set_a)

# 🧠 Explanation:
# Sets are unordered collections of unique elements.
# Useful for membership testing and eliminating duplicates.
# Set operations are efficient: average time complexity is O(1) for add/remove/check.
