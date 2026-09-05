#Day 31 --> 
'''
methods --> instance methods, class methods, static methods
usage of constructor
'''
'''
class Employee:
    """Employee class displaying employee details"""
    company = 'codegnan'
    def __init__(self):#Constructer
        self.name = input("Enter the employee name:")
        self.age = int(input("Enter the age:"))
        #self.role = input("Enter role:")
        while True:
            self.salary = int(input("Enter your salary:"))
            if self.salary == 0:
                print("Salary Cannot be 0, Please enter a positive integer")
            elif self.salary < 0:
                print("salary Cannot be a -ve number, please enter a positive number")
            else:
                break
        if self.salary <= 10000:
            self.role = 'Dept Frontdesk'
        elif 10001 <= self.salary <= 25000:
            self.role = 'Dept Admin'
        elif 25001 <= self.salary <= 50000:
            self.role = 'Dept Training'  
        elif self.salary > 50000:
            self.role = 'Manager'
    #instance methods
    def display_details(self):
        print(f'Name   : {self.name}',
            f'\nAge    : {self.age}',
            f'\nSalary : {self.salary}',
            f'\nRole   : {self.role}')         
emp1 = Employee()
emp1.display_details()
'''
'''
class product:
    platform = "amazon"
    def __init__(self, name, prize, discount):
        self.name = name
        self.prize = prize 
        self.discount = discount 
    def display_items(self):
        print(f"Item: {self.name} | Price: ${self.prize:.2f}")
    def apply_discount(self):
        discount_amount = self.prize * (self.discount / 100)
        self.prize = self.prize - discount_amount
        print(f"Applied a {self.discount}% discount!")

item1 = product("Laptop", 500, 10)

item1.display_items() 
item1.apply_discount() 
item1.display_items()
'''
'''
class Product:
    platform = 'amazon'
    delivery_charges = 50
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60
    def display_items(self):
        self.price = self.price + Product.delivery_charges
        print(f'item is {self.name} and price is {self.price}')
    @staticmethod
    def free_delivery(price):
        return price >= 35000
'''        
'''
obj1 = Product('oneplus',2000)
obj1.update_delivery()
obj1.display_items()
obj2 = Product('iphone',10000)
obj2.display_items()

obj1 = Product('laptop',45000)
obj1.display_items()
print(obj1.free_delivery(30000))
obj1.display_items()
print(obj1.__dict__)
'''


#use static and class methods but make sure free delivery should be applicable when the price > 30000, which means apply delivery charge as zero
#below 30000 delivery charge should be 60 as per class variable update.

class Product:

    platform = "Flipkart"
    delivery_charges = 50

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60

    def is_free_delivery(self):
        return self.price > 30000

    def display(self):

        if self.price <= 0:
            print("Invalid Price")
            return
        print("Product:", self.name)
        print("Price:", self.price)

        if self.is_free_delivery():
            print("Delivery Charges: 0")
            print("Free Delivery")
            print("Total Price:", self.price)
        else:
            print("Delivery Charges:", Product.delivery_charges)
            print("Total Price:", self.price + Product.delivery_charges)


# Update delivery charges from 50 to 60
Product.update_delivery()
product = Product('laptop',10000)
product.display()