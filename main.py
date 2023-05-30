class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount

    def check_balance(self):
        return self.account_balance


# Helper function to prompt user for input
def get_account_info():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    return (account_number, account_holder_name, initial_balance)


# Example usage:
accounts = []

while True:
    print("\nOptions:")
    print("1. Create new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_number, account_holder_name, initial_balance = get_account_info()
        new_account = BankAccount(account_number, account_holder_name, initial_balance)
        accounts.append(new_account)
        print("New account created!")
        print(accounts)
    elif choice == 2:
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        for account in accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                print("Amount deposited successfully!")
                break
        else:
            print("Account not found.")
    elif choice == 3:
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        for account in accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                print("Amount withdrawn successfully!")
                break
        else:
            print("Account not found or insufficient funds.")
    elif choice == 4:
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                print(f"Account balance: {account.check_balance()}")
                break
        else:
            print("Account not found.")
    elif choice == 5:
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
