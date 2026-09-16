from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def calculate_discount(self, amount):
        pass


class PercentageDiscount(Discount):

    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discount(self, amount):

        return amount * self.percentage / 100


class FlatDiscount(Discount):

    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def calculate_discount(self, amount):

        if self.discount_amount > amount:
            return amount

        return self.discount_amount


class NoDiscount(Discount):

    def calculate_discount(self, amount):

        return 0