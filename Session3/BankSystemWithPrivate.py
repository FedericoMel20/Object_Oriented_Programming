class BankAccount:
    accounts = []
    
    def __init__(self, account_holder, initial_deposit, pin):
        self.account_holder = account_holder  # Public attribute
        self._balance = initial_deposit  # Protected attribute
        self.__pin = pin  # Private attribute
        self.account_number = len(BankAccount.accounts) + 1
        BankAccount.accounts.append(self)
    
    @property
    def get_balance(self):
        return self._balance  # Getter for balance
    
    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Invalid amount. Balance update failed.")
    
    def verify_pin(self, pin):
        return self.__pin == pin  # Checks if PIN is correct
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount} into {self.account_holder}'s account. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ${amount} from {self.account_holder}'s account. New balance: ${self._balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Incorrect PIN. Withdrawal failed.")
    
    @classmethod
    def list_accounts(cls):
        if cls.accounts:
            print("\nList of Accounts:")
            for acc in cls.accounts:
                print(f"Account Number: {acc.account_number}, Name: {acc.account_holder}, Balance: ${acc.get_balance}")
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
        pin = input("Set your 4-digit PIN: ")
        BankAccount(name, initial_deposit, pin)
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
        pin = input("Enter your PIN: ")
        if 0 < acc_num <= len(BankAccount.accounts):
            BankAccount.accounts[acc_num - 1].withdraw(amount, pin)
        else:
            print("Invalid account number.")
    elif choice == "4":
        BankAccount.list_accounts()
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
