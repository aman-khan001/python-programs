# 📚 Python Program to Determine BMI Category


'''
    The bmi_category function takes a BMI value as input and returns the category of the BMI:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 24.9
    - Overweight: 25 <= BMI < 29.9
    - Obesity: BMI >= 30
'''

def bmi_category(bmi):
    """
    Determine the BMI category based on the given BMI value.

    Parameters:
    bmi (float): The Body Mass Index value.

    Returns:
    str: The category of the BMI.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
# Example usage
print("BMI Category:")
print("BMI 17.5:", bmi_category(17.5))  # Output: Underweight
print("BMI 22.0:", bmi_category(22.0))  # Output: Normal weight
print("BMI 27.5:", bmi_category(27.5))  # Output: Overweight