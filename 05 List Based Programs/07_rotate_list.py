# 📚 Python Program to Rotate a List by k Positions

'''  
  This program rotates a list to the right by k positions and returns the rotated list.
'''

def rotate_list(input_list, k):
    # Handle empty list or no rotation
    if not input_list or k == 0:
        return input_list
    # Normalize k to avoid unnecessary rotations
    k = k % len(input_list)
    # Rotate the list by slicing
    return input_list[-k:] + input_list[:-k]

# Example usage
input_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(input_list, k)
print("Original List:", input_list)
print("Rotated List:", rotated_list)

# 🧠 Explanation:
# The function `rotate_list` takes a list and an integer k as input and returns a new list that is rotated to the right by k positions.
# It first checks if the list is empty or if k is 0, in which case it returns the original list.
# It then normalizes k to ensure it's within the bounds of the list length.
# Finally, it performs the rotation by slicing the list and concatenating the two parts.