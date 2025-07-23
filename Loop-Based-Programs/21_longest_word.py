# 📚 Python Program: Longest Word in a Sentence

'''
    The longest_word function takes a sentence as input and returns the longest word in that sentence.
    It uses a for loop to iterate through each word in the sentence and keeps track of the longest word found so far.
'''

def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    longest = ""
    # Iterate through each word in the sentence
    for word in words:
        # Check if the current word is longer than the longest found so far
        if len(word) > len(longest):
            # Update the longest word found so far
            longest = word
    # Return the longest word
    return longest

# Example usage
sentence = input("Enter a sentence: ")
print(f"The longest word in the sentence is: '{longest_word(sentence)}'")
# Example output:
# Enter a sentence: The quick brown fox jumped over the lazy dog
# The longest word in the sentence is: 'jumped'