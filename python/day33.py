'''
OPP
Methods -> Instance methods, Class Methods, Static Methods
'''

# useage of Constru-====y7-==-7ctor
'''
class Employee:
    """Employee Class display Details"""
    company = "Codegnan" #class attribute
    def __init__(self):
        self.name = input("Enter the employee name:")
        self.age = int(input("Enter employee age:"))
        self.role = input("Enter employee Role:")
        self.salary = int(input("Enter "))
    # instance methods
    def display_details(self):
        print(f"Employee name is {self.name}, age is {self.age},role is {self.role}")

print(Employee.company)
emp1 = Employee()
print(dir(emp1))
emp1.display_details()
print(emp1.__dict__)
print(emp1.company)
'''
# use salary as another attribute and keep condition as 
'''
class Employee:
    """Employee Class display Details"""
    company = "Codegnan"  # class attribute

    def __init__(self):
        self.name = input("Enter the employee name:")
        self.age = int(input("Enter employee age:"))
        self.role = input("Enter employee Role:")
        self.salary = int(input("Enter employee salary:"))

        if self.salary == 0:
            print(f"{self.salary} is must be greater than 0")
        elif self.salary > 0:
            if self.salary <= 10000:
                print("Dept Frontdesk")
            elif self.salary > 10000 and self.salary <= 250000:
                print("Dept Admin")
            elif self.salary > 250000 and self.salary < 500000:
                print("Dept Training")
        else:
            print("Invalid salary")

    # instance methods
    def display_details(self):
        print(f"Employee name is {self.name}, age is {self.age}, role is {self.role}")
        print(f"Employee salary is {self.salary}")


emp2 = Employee()
emp2.display_details()
print(emp2.__dict__)'''

# using self to modify with attributes within class 
'''
class Product:
    platform="Amazon"
    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount
    def dis_item(self):
        print(f"Item is {self.name} and price is {self.price}")
    def apply_dis(self):
        self.price = self.price-(self.price* (self.discount/100))
        print(f"Final price is {self.price}")
obj1 = Product("Iphone",950000,15)
print(obj1.platform)
print(Product.platform)
obj1.dis_item()
obj1.apply_dis()
print(obj1.__dict__)
'''

# classmethod ---> @classmethod 
#staticmethod ---> @staticmethod
'''
class Product:

    platform = "Flipkart"
    delivery_charges = 50

    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60

    def display_items(self):
        self.price = self.price + Product.delivery_charges
        print(f'Item is {self.name} and price is {self.price}')


obj1 = Product("OnePlus", 15000)

print(obj1.platform)
Product.update_delivery() # we are acess class method
obj1.display_items()
print(Product.delivery_charges)
print(obj1.__dict__)
'''


# static delivery

class Product:

    platform = "Flipkart"
    delivery_charges = 50

    def _init_(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60

    def display_items(self):
        self.price = self.price + Product.delivery_charges
        print(f'Item is {self.name} and price is {self.price}')
    @staticmethod
    def free_dev(price):
        return price >=35000
'''
obj1 = Product("OnePlus", 15000)

print(obj1.platform)
Product.update_delivery() # we are acess class method
obj1.display_items()
print(Product.delivery_charges)
print(obj1._dict_)'''

obj1 = Product("Laptop",45000)

obj1.display_items()
print(obj1.free_dev(30000))
print(obj1.free_dev(36000))
print(obj1._dict_)

# use static and class method but amke sure  free delivery shold be applicable when the price > 30000
#where is develiry charages should v]be zero
# below 30000 should be 60 as per classs varible update  