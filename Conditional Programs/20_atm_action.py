# 📚 Python Program: Basic ATM simulation


'''
    The atm_action function takes the current balance and an action as input.
    It performs the specified action (withdraw, deposit, check_balance) and returns the updated balance
    along with a message indicating the result of the action.
'''

def atm_action(balance, action):
    # Check if the action is to withdraw money
    if action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        # Check if the withdrawal amount is greater than the current balance
        if amount > balance:

            return balance, "Insufficient funds." 

        else:
            balance -= amount
            return balance, f"Withdrew ${amount}. New balance is ${balance}."

    # Check if the action is to deposit money
    elif action == 'deposit':
        # Prompt user for the amount to deposit
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        # Return the updated balance after deposit
        return balance, f"Deposited ${amount}. New balance is ${balance}."

    # Check if the action is to check the balance
    elif action == 'check_balance':
        # Return the current balance
        return balance, f"Your current balance is ${balance}."
    
    # If the action is not recognized
    else:
        # Return the current balance and an error message
        return balance, "Invalid action."
    
# Example usage
current_balance = 1000.0  # Initial balance
action = input("Enter action (withdraw, deposit, check_balance): ").strip().lower()
    
new_balance, message = atm_action(current_balance, action)
print(message)

# Example output:
# Enter action (withdraw, deposit, check_balance): withdraw
# Enter amount to withdraw: 200
# Withdrew $200. New balance is $800.0.