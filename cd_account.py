"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, 0)
    print(f"Created CD account with initial balance: ${balance:.2f}")
    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/100 * months/12)
    print(f"Interest earned: ${interest_earned:.2f}")
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    print(f"Updated balance: ${updated_balance:.2f}")
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_balance)
    print(f"Set balance to: ${cd_account.balance:.2f}")
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest_earned)
    print(f"Set interest to: ${cd_account.interest:.2f}")
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    print(f"Returning updated balance: ${updated_balance:.2f} and interest earned: ${interest_earned:.2f}")
    return updated_balance, interest_earned
if __name__ == "__main__":
    initial_balance = 100
    interest_rate = 5
    months = 12

    print(f"Creating CD account with:")
    print(f"Initial balance: ${initial_balance:.2f}")
    print(f"Interest rate: {interest_rate}%")
    print(f"Term: {months} months\n")

    final_balance, interest = create_cd_account(initial_balance, interest_rate, months)