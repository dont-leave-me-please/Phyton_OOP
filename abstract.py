from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")


class BankPayment(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using Bank Transfer")


payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankPayment()
]

for payment in payments:
    payment.pay(100)