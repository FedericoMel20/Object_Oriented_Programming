class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")

    def display_details(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    WITHDRAWAL_LIMIT = 500
    
    def withdraw(self, amount):
        if amount > self.WITHDRAWAL_LIMIT:
            print(f"Withdrawal limit exceeded! Max allowed: ${self.WITHDRAWAL_LIMIT}")
        else:
            super().withdraw(amount)

class PremiumSavingsAccount(SavingsAccount):
    WITHDRAWAL_LIMIT = 2000

# Testing
basic_account = BankAccount("12345", 1000)
savings_account = SavingsAccount("67890", 1500)
premium_account = PremiumSavingsAccount("54321", 5000)

basic_account.deposit(500)
basic_account.withdraw(700)
basic_account.display_details()

savings_account.withdraw(600)  # Should fail
savings_account.withdraw(400)  # Should succeed
savings_account.display_details()

premium_account.withdraw(1800)  # Should succeed
premium_account.withdraw(2500)  # Should fail
premium_account.display_details()
