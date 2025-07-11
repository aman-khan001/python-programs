# 📚 Python Program to Check Leap Year

"""
  This program checks if a given year is a leap year.

  A year is a leap year if:
  - It is divisible by 4;
  - If it is divisible by 100, it must also be divisible by 400.
"""



def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

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