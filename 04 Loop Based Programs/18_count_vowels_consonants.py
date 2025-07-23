# 📚 Python Program: Count Vowels and Consonants

'''
    This program counts the number of vowels and consonants in a given text.

    The count_vowels_consonents function iterates through each character in the text,
    checking if it is a vowel or consonant, and updates the respective counts.
'''

def count_vowels_consonents(text):
    # Define sets of vowels and consonants
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0
    
    # Loop through each character in the text
    for char in text:
        # Check if the character is a vowel or consonant
        if char in vowels:
            # Increment the vowel count
            vowel_count += 1
        elif char in consonants:
            # Increment the consonant count
            consonant_count += 1
    # Return the counts of vowels and consonants    
    return vowel_count, consonant_count

# Example usage
text = input("Enter a text: ")
vowel_count, consonant_count = count_vowels_consonents(text)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
# Example output:
# Enter a text: Hello World!
# Number of vowels: 3
# Number of consonants: 7
