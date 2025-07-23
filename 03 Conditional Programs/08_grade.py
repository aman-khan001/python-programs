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
    
    if score >= 90:
        # Return 'A' for scores 90 and above
        return 'A'
    elif score >= 80:
        # Return 'B' for scores 80 to 89
        return 'B'
    elif score >= 70:
        # Return 'C' for scores 70 to 79
        return 'C'
    elif score >= 60:
        # Return 'D' for scores 60 to 69
        return 'D'
    else:
        # Return 'F' for scores below 60
        return 'F'
    
# Example usage
print("Grade for score 95:", grade(95))  # Output: A
print("Grade for score 85:", grade(85))  # Output: B
print("Grade for score 75:", grade(75))  # Output: C