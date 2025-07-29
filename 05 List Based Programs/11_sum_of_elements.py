# 📚 Python Program to Calculate the Sum of Elements in a List

'''  
  This program calculates the sum of all elements in a list of numbers.
'''

def sum_of_elements(numbers):
    total = 0
    # Iterate through the list and add each number to total
    for num in numbers:
        total += num
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print("List of numbers:", numbers)
print("Sum of elements:", result)

# 🧠 Explanation:
# The sum_of_elements function takes a list of numbers as input and returns the sum of its elements.
# It initializes a variable total to 0, iterates through each number in the list, adds it to total,
# and finally returns the total sum.
