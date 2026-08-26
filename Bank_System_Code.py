from decimal import Decimal, InvalidOperation
from datetime import datetime


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when an amount is zero, negative, or invalid."""
    pass


class BankAccount:
    """A simple bank account supporting deposits, withdrawals, and transaction history."""

    def __init__(self, owner: str, initial_balance: Decimal = Decimal("0.00")):
        self.owner = owner
        self.balance = Decimal(initial_balance)
        self.transaction_history = []

    def _validate_amount(self, amount: Decimal) -> None:
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

    def deposit(self, amount: Decimal) -> None:
        """Deposit a positive amount into the account."""
        self._validate_amount(amount)
        self.balance += amount
        self._log_transaction("Deposit", amount)
        print(f"Deposited: ${amount:.2f} | New Balance: ${self.balance:.2f}")

    def withdraw(self, amount: Decimal) -> None:
        """Withdraw a positive amount if sufficient funds are available."""
        self._validate_amount(amount)
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f}. Balance is ${self.balance:.2f}."
            )
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)
        print(f"Withdrew: ${amount:.2f} | New Balance: ${self.balance:.2f}")

    def _log_transaction(self, kind: str, amount: Decimal) -> None:
        self.transaction_history.append({
            "type": kind,
            "amount": amount,
            "balance_after": self.balance,
            "timestamp": datetime.now(),
        })

    def print_statement(self) -> None:
        """Print a simple transaction statement."""
        print(f"\n--- Statement for {self.owner} ---")
        for tx in self.transaction_history:
            ts = tx["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{ts}] {tx['type']:<10} ${tx['amount']:.2f}  Balance: ${tx['balance_after']:.2f}")
        print(f"Current Balance: ${self.balance:.2f}\n")


def get_valid_amount(prompt: str) -> Decimal:
    """Prompt the user until a valid positive decimal amount is entered."""
    while True:
        try:
            value = Decimal(input(prompt))
            if value <= 0:
                print("Please enter a value greater than zero.")
                continue
            return value
        except InvalidOperation:
            print("Invalid input. Please enter a numeric amount (e.g., 100.50).")


def main():
    name = input("Enter account holder's name: ").strip() or "Account Holder"
    account = BankAccount(owner=name)

    deposit_amount = get_valid_amount("Enter the amount to deposit: $")
    account.deposit(deposit_amount)

    withdraw_amount = get_valid_amount("Enter the amount to withdraw: $")
    try:
        account.withdraw(withdraw_amount)
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    account.print_statement()


if __name__ == "__main__":
    main()