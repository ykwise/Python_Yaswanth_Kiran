from food import FoodItem


class Restaurant:

    def __init__(self, restaurant_id, name, location, owner):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.owner = owner
        self.menu = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)
        print(f"{food_item.name} added successfully")

    def remove_food_item(self, item_id):

        for food_item in self.menu:
            if food_item.item_id == item_id:
                self.menu.remove(food_item)
                print(f"{food_item.name} removed successfully")
                return

        print(f"Food item with ID {item_id} not found")

    def update_food_price(self, item_id, new_price):

        for food_item in self.menu:
            if food_item.item_id == item_id:
                food_item.update_price(new_price)
                return

        print(f"Food item with ID {item_id} not found")

    def display_menu(self):

        print(f"\n===== {self.name} MENU =====")

        for food_item in self.menu:
            food_item.display()