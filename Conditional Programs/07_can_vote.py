# 📚 Python Program to Check Voting Eligibility

"""
  This program checks if a person is eligible to vote based on their age.
  A person is eligible to vote if they are 18 years old or older.
"""

def can_vote(age):
    """
    Determines if a person is eligible to vote based on their age.
    
    Args:
    age (int): The age of the person.
    
    Returns:
    str: A message indicating whether the person can vote or not.
    """
    if age >= 18:
        return "You can vote."
    else:
        return "You cannot vote yet."
    
# Example usage
print("Voting Eligibility:")
print("Age 20:", can_vote(20))  # Output: You can vote.
print("Age 17:", can_vote(17))  # Output: You cannot vote yet.
