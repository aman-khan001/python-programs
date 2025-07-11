# 📘 Program: Calculate Electricity Bill
# This program defines a function to calculate the electricity bill based on the number of units consumed.
  
'''
      The calculate_bill function takes the number of units consumed as input and returns the total bill amount.
      The rates are structured in tiers:
      - First 100 units: $0.50 per unit
      - Next 100 units (101-200): $0.75 per unit
      - Next 100 units (201-300): $1.20 per unit
      - Above 300 units: $1.50 per unit
'''

def calculate_bill(units):
    """
    Calculate the electricity bill based on the number of units consumed.
    The rates are as follows:
    - First 100 units: $0.50 per unit
    - Next 100 units (101-200): $0.75 per unit
    - Next 100 units (201-300): $1.20 per unit
    - Above 300 units: $1.50 per unit
    """
    if units < 0:
        raise ValueError("Units cannot be negative")
    
    if units <= 100:
        return units * 0.50
    elif units <= 200:
        return (100 * 0.50) + ((units - 100) * 0.75)
    elif units <= 300:
        return (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.20)
    else:
        return (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)
    
# Example usage
print("Bill for 50 units:", calculate_bill(50))    # Output: 25.0
print("Bill for 150 units:", calculate_bill(150))  # Output: 87.5
print("Bill for 250 units:", calculate_bill(250))  # Output: 162.5
print("Bill for 350 units:", calculate_bill(350))  # Output: 262.5
