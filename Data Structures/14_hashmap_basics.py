# 📘 Program: Hash Map (Dictionary) Usage in Python
# This program demonstrates basic operations on a Python dictionary

'''
  A hash map (or dictionary) is a data structure that stores key-value pairs.
  It allows for fast access, insertion, and deletion of elements based on keys.
'''


# Creating a dictionary (hash map)
student_marks = {
    "Oliver": 85,
    "Olivia": 90,
    "Liam": 78
}

# Accessing a value by key
print("Oliver's Marks:", student_marks["Oliver"])

# Adding a new key-value pair
student_marks["Olivia"] = 88
print("Added Olivia:", student_marks)

# Updating an existing value
student_marks["Liam"] = 82
print("Updated Liam's marks:", student_marks)

# Deleting a key-value pair
del student_marks["Liam"]
print("After deleting Liam:", student_marks)

# Iterating through dictionary
print("All student marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# Checking if a key exists
if "Oliver" in student_marks:
    print("Oliver is in the dictionary.")
else:
    print("Oliver is not in the dictionary.")


# 🧠 Explanation:
# Dictionaries (hash maps) use key-value pairs.
# They allow fast access, addition, update, and deletion by key.
# Time complexity: O(1) on average for lookups and insertions.
