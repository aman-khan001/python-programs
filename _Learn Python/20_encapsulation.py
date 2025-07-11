# 📘 Program: Encapsulation in Python (OOP)
# This program demonstrates how to use private variables and getter/setter methods

'''
  Encapsulation is a fundamental concept in Object-Oriented Programming (OOP) that restricts direct access to an object's attributes and methods.
'''


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable using double underscore

    def get_balance(self):
        return self.__balance  # Getter method

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance or invalid amount.")

# Creating an object of BankAccount
account = BankAccount("Alex", 1000)

# Using methods to access and modify balance
print("Balance:", account.get_balance())  # Accessing private variable
account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())

# 🧠 Explanation:
# Encapsulation hides the internal state using private variables.
# Access to private data is done through methods (getters/setters).
# This prevents direct access and modification, ensuring data integrity.
