# 📚 Python Program to Count Even and Odd Numbers in a List

'''  
  This program counts the number of even and odd integers in a list.
'''

def count_even_odd(lst):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    for num in lst:
        if num % 2 == 0:
            # If the number is even, increment the even count
            even_count += 1
        else:
            # If the number is odd, increment the odd count
            odd_count += 1
            
    return even_count, odd_count

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(my_list)
print("Even count:", even_count)
print("Odd count:", odd_count)

# 🧠 Explanation:
# The function count_even_odd takes a list of integers and counts the number of even and odd integers in it.
# It iterates through the list, checking each number's parity and updating the respective counters.
