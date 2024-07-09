# Write a program to simulate saving account processing in a bank using constructors. Create Deposit and Withdraw with other member function and Check for Validation while withdrawing the amount. Raise the appropriate exceptions when depositing and withdrawing an incorrect mount. Display appropriate messages

class SavingsAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")

    def display_balance(self):
        print(f"Account balance: {self.balance:.2f}")

account = SavingsAccount("12345678", "Kiran")
account.withdraw(200.0)