class FoodItem:

    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.is_available = True

    def update_price(self, price):
        if price > 0:
            self.price = price
        else:
            print("Price should be greater than 0!")

    def mark_available(self):
        self.is_available = True

    def mark_unavailable(self):
        self.is_available = False

    def display(self):
        status = "Available" if self.is_available else "Not Available"

        print(
            f"{self.item_id}. {self.name} - ₹{self.price} - "
            f"{self.category} - {status}"
        )