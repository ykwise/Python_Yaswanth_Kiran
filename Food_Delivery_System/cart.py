from food import FoodItem
class CartItem:

    def __init__(self,food_item,quantity=1):
        self.food_item = food_item
        self.quantity = quantity
        

    def increase_quantity(self):
        self.quantity +=1

    def decrease_qunatity(self):
        if(self.quantity > 1):
            self.quantity -= 1

    def calculate_item_total(self):
        return self.food_item.price * self.quantity

    def display(self):
        total = self.calculate_item_total()

        print(
            f"{self.food_item.name} "
            f"{self.food_item.price}rs x {self.quantity} = {total}rs"
        )

class Cart:

    def __init__(self):
         self.items = []

    def add_item(self,food_item):

        for cart_item in self.items:
            if cart_item.food_item.item_id == food_item.item_id:
                cart_item.increase_quantity()
                return


        new_cart_item = CartItem(food_item)
        self.items.append(new_cart_item)

    def remove_item(self,item_id):

        for cart_item in self.items:
            if cart_item.food_item.item_id == item_id:
                self.items.remove(cart_item)
                print(f"{cart_item.food_item.name} removed from cart")
                return
        print("Food Item With given Item Id not found")

    def update_quantity(self,item_id,quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        for cart_item in self.items:
            if cart_item.food_item.item_id == item_id:
                cart_item.quantity = quantity
                return

        print("Food Item Not Found")

    def calculate_subtotal(self):
        subtotal = 0

        for cart_item in self.items:
            subtotal+= cart_item.calculate_item_total()

        return subtotal

    def display_cart(self):
        print("\n==== CART ====")

        if not self.items:
            print("Cart is Empty")
            return

        for cart_item in self.items:
            cart_item.display()

        print(f"\nSubtotal: {self.calculate_subtotal()}rs")

        def clear_cart(self):
            self.items.clear()
            print("Cart cleared")
        

        
    