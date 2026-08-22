from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(Payment):

    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(f"Paid ${self.amount} using Credit Card")


payment = CreditCardPayment(100, "1234")

payment.pay()