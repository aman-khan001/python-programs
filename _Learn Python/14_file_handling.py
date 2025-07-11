# 📘 Program: File Handling in Python
# This program demonstrates how to write to and read from a text file

'''
  File handling is the process of reading from and writing to files in a computer's file system.
'''

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("We are writing this to a file using Python!\n")

# Reading from the same file
with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire content of the file
    print("📂 File Content:")
    print(content)

# 🧠 How it works:
# 'with open' ensures the file is properly closed after its block
# 'w' mode = write (creates file if not exists, overwrites if it does)
# 'r' mode = read
