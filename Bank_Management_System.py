class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Successfully!")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Funds!")
account = BankAccount()
deposit_amount = float(input("Enter the amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter the amount to withdraw: "))
account.withdraw(withdraw_amount)
