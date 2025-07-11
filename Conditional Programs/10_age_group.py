# 📚 Python Program to Determine Age Group

"""
  This program determines the age group of a person based on their age.
  The age groups are defined as follows:
  - Child: 0-12 years
  - Teenager: 13-19 years
  - Adult: 20-64 years
  - Senior Citizen: 65 years and older
"""

def age_group(age):
    """
    Determines the age group of a person based on their age.
    
    Args:
    age (int): The age of the person.
    
    Returns:
    str: A message indicating the age group of the person.
    """
    if age < 0:
        return "Invalid age."
    elif age < 13:
        return "You are a child."
    elif age < 20:
        return "You are a teenager."
    elif age < 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."
    
# Example usage
print("Age Group:")
print("Age 10:", age_group(10))    # Output: You are a child.
print("Age 15:", age_group(15))    # Output: You are a teenager.
print("Age 30:", age_group(30))    # Output: You are an adult.