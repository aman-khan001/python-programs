# 🐥 Program: Working with Dictionaries


'''    
    A dictionary is a collection of key-value pairs.
    It is unordered, changeable, and does not allow duplicates.
'''

# Creating a dictionary of student details
student = {
    "name": "Oliver",
    "age": 21,
    "course": "Python"
}

# Printing the entire dictionary
print("Student Info:", student)

# Accessing values by keys
print("Name:", student["name"])      # Output: Oliver
print("Age:", student["age"])        # Output: 21

# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Modifying an existing value
student["age"] = 22
print("After updating age:", student)

# Iterating through dictionary
print("All details:")
for key, value in student.items():
    print(key + ":", value)

# Removing a key-value pair
del student["course"]
print("After removing course:", student)

# Checking if a key exists
if "name" in student:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")
# Getting all keys and values
print("Keys:", student.keys())        # Output: dict_keys(['name', 'age', 'grade'])
print("Values:", student.values())    # Output: dict_values(['Oliver', 22, 'A'])

# Getting the length of the dictionary
print("Number of items in dictionary:", len(student))  # Output: 3

# Nested dictionaries - Dictionaries can contain other dictionaries
nested_student = {
    "student1": {
        "name": "Oliver",
        "age": 21
    },
    "student2": {
        "name": "Riya",
        "age": 22
    }
}
print("Nested Student Info:", nested_student)

# Accessing nested dictionary values
print("Student1 Name:", nested_student["student1"]["name"])  # Output: Oliver
print("Student2 Age:", nested_student["student2"]["age"])    # Output: 22

# Using dictionaries in functions - Passing a dictionary to a function
def print_student_info(student_dict):
    for key, value in student_dict.items():
        print(key + ":", value)
# Calling the function with the student dictionary
print_student_info(student)  # Output: Name: Oliver, Age: 22, Grade: A


# Using dictionaries in lists - Lists can contain dictionaries
students_list = [
    {"name": "Oliver", "age": 21},
    {"name": "Riya", "age": 22}
]
print("Students List:")

for student in students_list:
    print("Name:", student["name"], ", Age:", student["age"])
# Output: Name: Oliver , Age: 21
# Output: Name: Riya , Age: 22
    
# Using dictionaries as keys in other dictionaries
fruits_dict = {
    "apple": {"color": "red", "taste": "sweet"},
    "banana": {"color": "yellow", "taste": "sweet"}
}
print("Fruits Dictionary:")
for fruit, details in fruits_dict.items():
    print(fruit + ":", details)
# Output: apple: {'color': 'red', 'taste': 'sweet'}
# Output: banana: {'color': 'yellow', 'taste': 'sweet'}
    
# Using dictionary comprehension to create a new dictionary
squared_numbers = {x: x**2 for x in range(1, 6)}

print("Squared Numbers Dictionary:", squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging dictionaries - Combining two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using the get method to access values safely
print("Get Name:", student.get("name", "Not Found"))  # Output: Oliver
print("Get Course:", student.get("course", "Not Found"))  # Output: Not Found


# Using the pop method to remove a key-value pair and return the value
removed_value = student.pop("grade", "Not Found")
print("Removed Grade:", removed_value)  # Output: A
print("After popping grade:", student)  # Output: {'name': 'Oliver', 'age': 22, 'hobby': 'Reading'}

# Using the popitem method to remove and return the last inserted key-value pair
last_item = student.popitem()
print("Last Item Removed:", last_item)  # Output: ('hobby', 'Reading')
print("After popping last item:", student)  # Output: {'name': 'Oliver', 'age': 22}

# Using the clear method to remove all items from the dictionary
student.clear()
print("After clearing dictionary:", student)  # Output: {}

# Creating a new dictionary with default values
default_student = dict.fromkeys(["name", "age", "course"], "Unknown")
print("Default Student Dictionary:", default_student)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'course': 'Unknown'}

# Using the update method to merge another dictionary
update_dict = {"name": "Riya", "age": 22}
default_student.update(update_dict)
print("After update:", default_student)  # Output: {'name': 'Riya', 'age': 22, 'course': 'Unknown'}

# Using the items method to get key-value pairs as tuples
items = default_student.items()
print("Items in Default Student Dictionary:", items)  # Output: dict_items([('name', 'Riya'), ('age', 22), ('course', 'Unknown')])

# Using the keys method to get all keys
keys = default_student.keys()
print("Keys in Default Student Dictionary:", keys)  # Output: dict_keys(['name', 'age', 'course'])

# Using the values method to get all values
values = default_student.values()
print("Values in Default Student Dictionary:", values)  # Output: dict_values(['Riya', 22, 'Unknown'])

# Using the copy method to create a shallow copy of the dictionary
copied_student = default_student.copy()
print("Copied Student Dictionary:", copied_student)  # Output: {'name': 'Riya', 'age': 22, 'course': 'Unknown'}

# Using the dictionary constructor to create a dictionary from a list of tuples
tuple_list = [("name", "Oliver"), ("age", 21), ("course", "Python")]
constructed_student = dict(tuple_list)
print("Constructed Student Dictionary:", constructed_student)  # Output: {'name': 'Oliver', 'age': 21, 'course': 'Python'}
#
#  Using the dictionary constructor with keyword arguments
constructed_student_kw = dict(name="Oliver", age=21, course="Python")
print("Constructed Student Dictionary with kwargs:", constructed_student_kw)  # Output: {'name': 'Oliver', 'age': 21, 'course': 'Python'}

