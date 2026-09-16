from abc import ABC,abstractmethod

class user(ABC):
    def __init__(self,id,name,email,phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def login(self):
        print(f"{self.name} logged in")

    def logout(self):
        print(f"{self.name} logged out")

    @abstractmethod
    def get_role(self):
        pass


#Customer
class Customer(user):
    def get_role(self):
        return f"{self.name}: Customer"
    
    def place_order(self):
        print(f"{self.name} has placed an order.")
#Owner
class RestrauntOwner(user):
    def get_role(self):
        return f"{self.name}: Restraunt Owner"
    
    def manage_restraunt(self):
        print(f"Currently {self.name} is managing the restraunt.")

#Delivery Partner
class DeliveryPartner(user):
    def get_role(self):
        return f"{self.name}: Delivery Partner"

    def accept_delivery(self):
        print(f"{self.name} has accepted delivery.")

#Admin
class Admin(user):
    def get_role(self):
        return f"{self.name}: Admin"

    def manage_system(self):
        print(f"{self.name} is managing the system.")

        
