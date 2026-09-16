from abc import ABC, abstractmethod
from enum import Enum

from order import OrderStatus


class Vehicle(ABC):

    @abstractmethod
    def get_delivery_charge(self, distance):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass


class Bike(Vehicle):

    def get_delivery_charge(self, distance):
        return distance * 10

    def get_vehicle_type(self):
        return "Bike"


class Scooter(Vehicle):

    def get_delivery_charge(self, distance):
        return distance * 12

    def get_vehicle_type(self):
        return "Scooter"


class Cycle(Vehicle):

    def get_delivery_charge(self, distance):
        return distance * 5

    def get_vehicle_type(self):
        return "Cycle"


class AvailabilityStatus(Enum):

    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"
    OFFLINE = "OFFLINE"


class DeliveryPartner:

    def __init__(self, partner_id, name, vehicle):

        self.partner_id = partner_id
        self.name = name
        self.vehicle = vehicle

        self.availability_status = (
            AvailabilityStatus.AVAILABLE
        )

        self.current_order = None

    def accept_order(self, order):

        if self.availability_status != AvailabilityStatus.AVAILABLE:
            print("Delivery partner is not available")
            return False

        if order.status != OrderStatus.CONFIRMED:
            print("Order must be confirmed before delivery")
            return False

        self.current_order = order

        self.availability_status = (
            AvailabilityStatus.BUSY
        )

        print(
            f"{self.name} accepted "
            f"Order #{order.order_id}"
        )

        return True

    def pickup_order(self):

        if self.current_order is None:
            print("No order assigned")
            return

        self.current_order.change_status(
            OrderStatus.OUT_FOR_DELIVERY
        )

        print(
            f"{self.name} picked up "
            f"Order #{self.current_order.order_id}"
        )

    def deliver_order(self):

        if self.current_order is None:
            print("No order assigned")
            return

        self.current_order.change_status(
            OrderStatus.DELIVERED
        )

        print(
            f"{self.name} delivered "
            f"Order #{self.current_order.order_id}"
        )

        self.current_order = None

        self.availability_status = (
            AvailabilityStatus.AVAILABLE
        )

    def calculate_delivery_charge(self, distance):

        if distance < 0:
            print("Distance cannot be negative")
            return 0

        return self.vehicle.get_delivery_charge(distance)

    def display(self):

        print("\n===== DELIVERY PARTNER =====")

        print(f"Partner ID: {self.partner_id}")
        print(f"Name: {self.name}")

        print(
            f"Vehicle: "
            f"{self.vehicle.get_vehicle_type()}"
        )

        print(
            f"Status: "
            f"{self.availability_status.value}"
        )

        if self.current_order:
            print(
                f"Current Order: "
                f"#{self.current_order.order_id}"
            )
        else:
            print("Current Order: None")