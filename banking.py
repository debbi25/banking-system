class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
            return

        self.balance += amount
        self.transactions.append(
            f"Deposited: Rs.{amount:.2f}"
        )

        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.transactions.append(
            f"Withdrawn: Rs.{amount:.2f}"
        )

        print("Amount withdrawn successfully.")

    def display_account(self):
        print("\n--------------------------------")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.name)
        print("Account Type   :", self.account_type())
        print("Balance        : Rs.", round(self.balance, 2))
        print("--------------------------------")

    def account_type(self):
        return "Bank Account"

    def show_transactions(self):
        print("\n----- Transaction History -----")

        if not self.transactions:
            print("No transactions available.")
            return

        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)
        self.interest_rate = 4

    def account_type(self):
        return "Savings Account"

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

        self.transactions.append(
            f"Interest added: Rs.{interest:.2f}"
        )

        print(
            f"Interest of Rs.{interest:.2f} added."
        )


class CurrentAccount(BankAccount):
    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):
        minimum_balance = 1000

        if self.balance - amount < minimum_balance:
            print(
                "Minimum balance of Rs.1000 "
                "must be maintained."
            )
            return

        super().withdraw(amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("\n----- Create Account -----")

        try:
            account_number = input(
                "Enter account number: "
            )

            if account_number in self.accounts:
                print("Account number already exists.")
                return

            name = input("Enter account holder name: ")

            balance = float(
                input("Enter initial deposit: ")
            )

            if balance < 0:
                print("Balance cannot be negative.")
                return

            print("\n1. Savings Account")
            print("2. Current Account")

            choice = input("Enter account type: ")

            if choice == "1":
                account = SavingsAccount(
                    account_number,
                    name,
                    balance
                )

            elif choice == "2":
                account = CurrentAccount(
                    account_number,
                    name,
                    balance
                )

            else:
                print("Invalid account type.")
                return

            self.accounts[account_number] = account

            print("Account created successfully.")

        except ValueError:
            print("Please enter a valid amount.")

    def find_account(self):
        account_number = input(
            "Enter account number: "
        )

        if account_number not in self.accounts:
            print("Account not found.")
            return None

        return self.accounts[account_number]

    def deposit(self):
        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter amount to deposit: ")
            )

            account.deposit(amount)

        except ValueError:
            print("Invalid amount.")

    def withdraw(self):
        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter amount to withdraw: ")
            )

            account.withdraw(amount)

        except ValueError:
            print("Invalid amount.")

    def check_balance(self):
        account = self.find_account()

        if account:
            account.display_account()

    def show_transactions(self):
        account = self.find_account()

        if account:
            account.show_transactions()

    def add_interest(self):
        account = self.find_account()

        if account is None:
            return

        if isinstance(account, SavingsAccount):
            account.add_interest()
        else:
            print(
                "Interest is available only "
                "for savings accounts."
            )

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return

        for account in self.accounts.values():
            account.display_account()

    def run(self):
        while True:
            print("\n================================")
            print("        BANK MANAGEMENT")
            print("================================")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Add Interest")
            print("7. Display All Accounts")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.check_balance()

            elif choice == "5":
                self.show_transactions()

            elif choice == "6":
                self.add_interest()

            elif choice == "7":
                self.display_all_accounts()

            elif choice == "8":
                print("Thank you for using the bank system.")
                break

            else:
                print("Invalid choice.")


bank = Bank()
bank.run()