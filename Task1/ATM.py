class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    # Deposit function
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: Rs.{amount}")
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Deposit amount must be a positive or natural number.")

    # Withdraw function
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawn: Rs.{amount}")
                print(f"Rs.{amount} withdrawn successfully.")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be a natural number.")

    # Check balance function
    def check_balance(self):
        print(f"Your current balance is: Rs.{self.balance}")

    # Show transaction history function
    def show_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions done yet.")

    # Main function for ATM
    def main():
        print("Welcome to Snehal's ATM!")
        atm = ATM(balance=1000)

        while True:
            # Menu Options
            print("\nPlease choose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Show Transaction History")
            print("5. Exit")

            # User input
            choice = input("Enter your choice: ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '4':
                atm.show_transaction_history()
            elif choice == '5':
                print("Thank you for visiting this ATM. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run main function
if __name__ == "__main__":
    ATM.main()