# 📚 Python Program to convert Celsius to Fahrenheit
# This program defines a function to convert temperature from Celsius to Fahrenheit.

'''
    The celsius_to_fahrenheit function takes a temperature in Celsius as input
    and returns the equivalent temperature in Fahrenheit using the formula:
    Fahrenheit = (Celsius * 9/5) + 32.
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage
print("Celsius to Fahrenheit:")
print("0°C =", celsius_to_fahrenheit(0), "°F")   # Output: 32.0
print("100°C =", celsius_to_fahrenheit(100), "°F")  # Output: 212.0
