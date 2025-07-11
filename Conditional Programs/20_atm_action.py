# 📚 Python Program: Basic ATM simulation
# This program defines a function to perform ATM actions such as withdrawing, depositing, and checking balance.

'''
    The atm_action function takes the current balance and an action as input.
    It performs the specified action (withdraw, deposit, check_balance) and returns the updated balance
    along with a message indicating the result of the action.
'''

def atm_action(balance, action):
    """
    Perform an ATM action based on the user's input.

    Parameters:
    balance (float): The current balance in the account.
    action (str): The action to perform ('withdraw', 'deposit', 'check_balance').

    Returns:
    tuple: Updated balance and a message indicating the result of the action.
    """
    if action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            return balance, "Insufficient funds."
        else:
            balance -= amount
            return balance, f"Withdrew ${amount}. New balance is ${balance}."

    elif action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        return balance, f"Deposited ${amount}. New balance is ${balance}."

    elif action == 'check_balance':
        return balance, f"Your current balance is ${balance}."
    
    else:
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