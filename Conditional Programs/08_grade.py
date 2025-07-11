# 📚 Python Program to Determine Grade Based on Score

'''
    The grade function takes a score as input and returns the corresponding grade.
    The grading scale is as follows:
    - A: 90 and above
    - B: 80 to 89
    - C: 70 to 79
    - D: 60 to 69
    - F: Below 60
'''

def grade(score):
    """
    Returns the grade based on the score.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
# Example usage
print("Grade for score 95:", grade(95))  # Output: A
print("Grade for score 85:", grade(85))  # Output: B
print("Grade for score 75:", grade(75))  # Output: C