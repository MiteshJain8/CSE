# Develop a python program to create a class called as BankAccount with attributes like CustName, AccountNumber, Balance, TypeofAccount and Address. Write the methods for withdraw(), deposit() and displayDetails(). Create multiple objects and simulate the bank operations

class BankAccount:
    def __init__(self, cust_name, account_number, balance, type_of_account, address):
        self.cust_name = cust_name
        self.account_number = account_number
        self.balance = balance
        self.type_of_account = type_of_account
        self.address = address
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def display_details(self):
        print("Customer Name:", self.cust_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Type of Account:", self.type_of_account)
        print("Address:", self.address)

account1 = BankAccount("Pavitr Prabhakar", "123456789", 3000, "Savings", "Virar Mumbai")
account2 = BankAccount("Peter Parker", "987654321", 2000, "Current", "Queens NYC")
account1.deposit(500)
account2.withdraw(1000)
account1.display_details()
print()
account2.display_details()