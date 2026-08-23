class ABA:
    def pay(self):
        print("Pay with ABA")


class Visa:
    def pay(self):
        print("Pay with Visa")


class PayPal:
    def pay(self):
        print("Pay with PayPal")
payments = [ABA(), Visa(), PayPal()]

for payment in payments:
    payment.pay()