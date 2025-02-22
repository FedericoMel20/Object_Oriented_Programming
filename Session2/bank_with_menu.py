class BankAccount:
    accounts = []
    
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = len(BankAccount.accounts) + 1
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into {self.name}'s account. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s account. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    @classmethod
    def list_accounts(cls):
        if cls.accounts:
            print("\nList of Accounts:")
            for acc in cls.accounts:
                print(f"Account Number: {acc.account_number}, Name: {acc.name}, Balance: ${acc.balance}")
        else:
            print("No accounts available.")

# Menu-driven approach
while True:
    print("\nBanking System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. List Accounts")
    print("5. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        name = input("Enter account holder name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        BankAccount(name, initial_deposit)
        print(f"Account created successfully for {name}.")
    elif choice == "2":
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        if 0 < acc_num <= len(BankAccount.accounts):
            BankAccount.accounts[acc_num - 1].deposit(amount)
        else:
            print("Invalid account number.")
    elif choice == "3":
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        if 0 < acc_num <= len(BankAccount.accounts):
            BankAccount.accounts[acc_num - 1].withdraw(amount)
        else:
            print("Invalid account number.")
    elif choice == "4":
        BankAccount.list_accounts()
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
