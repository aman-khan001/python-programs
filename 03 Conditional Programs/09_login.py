# 📚 Python Program: Simple Login System


'''
    The login function prompts the user for a username and password,
    checks if they match predefined credentials, and prints a success or failure message.
'''

def login():
    print("Welcome to the login program!")
    
    # Prompt for username
    username = input("Enter your username: ")
    
    # Prompt for password
    password = input("Enter your password: ")
    
    # Check if the credentials are correct
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

login()

# Example usage
# Welcome to the login program!
# Enter your username: admin
# Enter your password: password123
# Login successful!

