class BankAccount:
    def __init__(self, account_balance: float):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance is {self.account_balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount}. New balance is {self.account_balance}.")
        elif amount > self.account_balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        return (f"Current Balance: {self.account_balance}")