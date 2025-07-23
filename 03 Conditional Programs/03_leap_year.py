# 📚 Python Program to Check Leap Year

"""
  This program checks if a given year is a leap year.

  A year is a leap year if:
  - It is divisible by 4;
  - If it is divisible by 100, it must also be divisible by 400.
"""


def is_leap_year(year):
    # Check if the year is a leap year
    if year < 0:
        return "Year cannot be negative."
    # A year is a leap year if it is divisible by 4 and not divisible by 100, or if it is divisible by 400
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False  
    
# Example usage
test_years = [2000, 2004, 1900, 2021, 2024]
for year in test_years:
    print(f"{year} is a leap year: {is_leap_year(year)}")
    
# Output:
# 2000 is a leap year: True
# 2004 is a leap year: True
# 1900 is a leap year: False
# 2021 is a leap year: False
# 2024 is a leap year: True