from food import FoodItem
from restraunt import Restaurant
from users import RestrauntOwner, Customer
from cart import Cart
from order import Order, OrderStatus
from discount import (
    Discount,
    PercentageDiscount,
    FlatDiscount,
    NoDiscount
)
from payment import (
    UPIPayment,
    CreditCardPayment,
    CashOnDeliveryPayment
)
from discount import PercentageDiscount
from payment import UPIPayment
from delivery import (
    DeliveryPartner,
    Bike,
    Scooter,
    Cycle
)
from notification import (
    EmailNotification,
    SMSNotification,
    PushNotification
)




owner = RestrauntOwner(
    2,
    "Priya",
    "priya@gmail.com",
    "9866746960"
)

customer = Customer(
    1,
    "Yaswanth",
    "yk@gmail.com",
    "9121959158"
)




restaurant = Restaurant(
    101,
    "Pizza Palace",
    "Hyderabad",
    owner
)




pizza = FoodItem(
    1,
    "Pizza",
    400,
    "Italian"
)

burger = FoodItem(
    2,
    "Burger",
    200,
    "Fast Food"
)

coke = FoodItem(
    3,
    "Coke",
    80,
    "Beverage"
)




restaurant.add_food_item(pizza)
restaurant.add_food_item(burger)
restaurant.add_food_item(coke)

restaurant.display_menu()




pizza.update_price(450)

restaurant.display_menu()

pizza.update_price(-100)

print()




cart = Cart()

cart.add_item(pizza)
cart.add_item(pizza)
cart.add_item(burger)
cart.add_item(coke)
cart.add_item(coke)

cart.display_cart()



cart.update_quantity(1, 3)


cart.remove_item(2)

cart.display_cart()




order = Order(
    1001,
    customer,
    restaurant
)

order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(coke, 2)

order.set_discount(
    PercentageDiscount(10)
)

order.set_delivery_charge(50)

order.set_payment(
    UPIPayment("yk@upi")
)

order.display_order()

order.make_payment()

partner = DeliveryPartner(
    501,
    "Arjun",
    Bike()
)

partner.display()
charge = partner.calculate_delivery_charge(5)

print(f"Delivery Charge: ₹{charge}")

order.change_status(OrderStatus.CONFIRMED)
partner.accept_order(order)
partner.pickup_order()
partner.deliver_order()

email = EmailNotification("yk@gmail.com")

sms = SMSNotification("9121959158")

push = PushNotification("DEVICE001")

message = "Your order #1001 has been confirmed!"

email.send(message)

print()

sms.send(message)

print()

push.send(message)

email = EmailNotification(customer.email)

sms = SMSNotification(customer.phone)

order.add_notification(email)
order.add_notification(sms)

order.send_notification(
    "Your order #1001 has been confirmed!"
)


