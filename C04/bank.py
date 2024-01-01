class BankAccount:
    def __init__(self, acc_num, acc_holder_name, acc_type, balance=0):
        self.acc_num = acc_num
        self.acc_holder_name = acc_holder_name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Withdrawal unsuccessful"
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def get_balance(self):
        return f"Current balance: ${self.balance}"


def main():
    print("Enter Account Details:")
    ac_no = int(input("\nEnter account number: "))
    name = input("\nEnter your name: ")
    acc_type = input("\nEnter account type:")
    initial_balance = float(input("\nEnter initial balance: "))  
    account = BankAccount(ac_no, name, acc_type, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            deposit_amount = float(input("Enter deposit amount: "))
            print(account.deposit(deposit_amount))
        elif choice == '2':
            withdraw_amount = float(input("Enter withdrawal amount: "))
            print(account.withdraw(withdraw_amount))
        elif choice == '3':
            print(account.get_balance())
        elif choice == '4':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
