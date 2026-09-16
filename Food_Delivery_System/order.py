from enum import Enum


class OrderStatus(Enum):
    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    PREPARING = "PREPARING"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class OrderItem:

    def __init__(self, food_item, quantity):
        self.food_item = food_item
        self.quantity = quantity

    def calculate_item_total(self):
        return self.food_item.price * self.quantity

    def display(self):
        total = self.calculate_item_total()

        print(
            f"{self.food_item.name} "
            f"₹{self.food_item.price} × {self.quantity} = ₹{total}"
        )


class Order:

    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant

        self.items = []
        self.notifications = []

        self.status = OrderStatus.PLACED

        self.discount = None
        self.delivery_charge = 0
        self.tax = 0
        self.total_amount = 0

        self.payment = None

    def add_item(self, food_item, quantity):

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        for order_item in self.items:

            if order_item.food_item.item_id == food_item.item_id:
                order_item.quantity += quantity
                return

        new_order_item = OrderItem(food_item, quantity)
        self.items.append(new_order_item)

    def calculate_subtotal(self):

        subtotal = 0

        for order_item in self.items:
            subtotal += order_item.calculate_item_total()

        return subtotal

    def set_discount(self, discount):
        self.discount = discount

    def calculate_discount(self):

        subtotal = self.calculate_subtotal()

        if self.discount is None:
            return 0

        return self.discount.calculate_discount(subtotal)

    def set_delivery_charge(self, charge):

        if charge < 0:
            print("Delivery charge cannot be negative")
            return

        self.delivery_charge = charge

    def calculate_tax(self, tax_percentage):

        amount_after_discount = (
            self.calculate_subtotal()
            - self.calculate_discount()
        )

        return amount_after_discount * tax_percentage / 100

    def calculate_total(self, tax_percentage=10):

        subtotal = self.calculate_subtotal()

        discount = self.calculate_discount()

        tax = self.calculate_tax(tax_percentage)

        self.tax = tax

        self.total_amount = (
            subtotal
            - discount
            + self.delivery_charge
            + tax
        )

        return self.total_amount

    def set_payment(self, payment):
        self.payment = payment

    def make_payment(self):

        if self.payment is None:
            print("Please select a payment method")
            return

        amount = self.calculate_total()

        self.payment.pay(amount)

    def change_status(self, new_status):

        if self.status == OrderStatus.DELIVERED:
            print("Order is already delivered")
            return

        if self.status == OrderStatus.CANCELLED:
            print("Order is already cancelled")
            return

        self.status = new_status

        print(
            f"Order #{self.order_id} status changed to "
            f"{self.status.value}"
        )

        message = (
        f"Your order #{self.order_id} "
        f"is now {self.status.value}"
    )

        self.send_notification(message)


    def cancel_order(self):

        if self.status == OrderStatus.DELIVERED:
            print("Delivered order cannot be cancelled")
            return

        self.status = OrderStatus.CANCELLED

        print(f"Order #{self.order_id} has been cancelled")

    def display_order(self):

        print("\n===== ORDER =====")

        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Restaurant: {self.restaurant.name}")

        print("\nItems:")

        for order_item in self.items:
            order_item.display()

        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        total = self.calculate_total()

        print(f"\nSubtotal: ₹{subtotal}")
        print(f"Discount: ₹{discount}")
        print(f"Delivery: ₹{self.delivery_charge}")
        print(f"Tax: ₹{self.tax}")
        print(f"Final Amount: ₹{total}")

        print(f"Order Status: {self.status.value}")


    def add_notification(self, notification):
        self.notifications.append(notification)

    def send_notification(self, message):

        for notification in self.notifications:
            notification.send(message)

        