# 📚 Python Program to Check if a Letter is a Vowel or a Consonant

"""
  This program checks if a given letter is a vowel or a consonant.
  A letter is considered a vowel if it is one of 'a', 'e', 'i', 'o', 'u' (case insensitive).
"""

def vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"
    # Check if the input is a single alphabetic character
    if len(letter) != 1 or not letter.isalpha():
        return "Please enter a single alphabetic character."
    
    # Convert to lowercase for case-insensitive comparison
    letter = letter.lower()  
    # Check if the letter is in the vowels string
    if letter in vowels:
        return "vowel"
    else:
        return "consonant"
    
# Example usage
print("Vowel or Consonant:")
print("a is a", vowel_or_consonant("a"))  # Output: vowel
print("b is a", vowel_or_consonant("b"))  # Output: consonant
print("E is a", vowel_or_consonant("E"))  # Output: vowel
print("z is a", vowel_or_consonant("z"))  # Output: consonant
# Example usage with invalid input
print("1 is a", vowel_or_consonant("1"))  # Output: Please enter a single alphabetic character.
print("# is a", vowel_or_consonant("#"))  # Output: Please enter a single alphabetic character.