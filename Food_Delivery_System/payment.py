from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPIPayment(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id
        self.status = "PENDING"

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")
        print(f"UPI ID: {self.upi_id}")

        self.status = "SUCCESS"

        print("UPI Payment Successful")

    def refund(self, amount):
        print(f"Refunding ₹{amount} to UPI ID: {self.upi_id}")

        self.status = "REFUNDED"

        print("UPI Refund Successful")


class CreditCardPayment(Payment):

    def __init__(self, card_number):
        self.card_number = card_number
        self.status = "PENDING"

    def pay(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}")
        print("Credit Card Payment Successful")

        self.status = "SUCCESS"

    def refund(self, amount):
        print(f"Refunding ₹{amount} to Credit Card")

        self.status = "REFUNDED"

        print("Credit Card Refund Successful")


class CashOnDeliveryPayment(Payment):

    def __init__(self):
        self.status = "PENDING"

    def pay(self, amount):
        print(f"Cash on Delivery selected for ₹{amount}")
        print("Payment will be collected during delivery")

        self.status = "PENDING"

    def refund(self, amount):
        print("Cash on Delivery does not require online refund")

        self.status = "REFUNDED"