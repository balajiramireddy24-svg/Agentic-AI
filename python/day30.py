# Day 30 --> Object Oriented Programming (OOP)

'''
Tokens --> Datatypes --> Control flow --> Functions --> Modules
Procedural oriented programming --> Functions
Object Oriented Programming --> objects, classes
OOP --> organizes data by treating them and objects/entities
* it object consists of two things -- > attributes(data),methods(behaviour) functions


class Class_name:
    attributes .... (variables)
    ...
    ...

    def fname(self):
        """ Doc string"""
        ...
        ...

#Wooden chair example --> chair as objects, class (blueprint which includes complete measurement,dimensions)
,user() scrap material wood, etc --> memory


Features of OOP:
1. Reusability
2. Modularity
3. abstraction
4. encapsulation
5. Inheritence
6. Polymorphism
'''
'''
class Product:
    """simple class demonstration with an example of e commerce process"""
    platform = 'amazon'
    def display_product(self):
        print(f'displaying products')
    def stock_available(self):
        print(f'stock is available')

book = Product()
print(book.platform)
book.display_product()
book.stock_available()

mobile = Product()
mobile.display_product()
#Product --> class, platform --> attributes, display_product, stock_available --> methods..
'''

class Product:
    """usage of class with instance attributes"""
    platform = 'amazon' #class attribute
    product_lst = []
    def store_products(this,name,price):
        this.name = name
        this.price = price
    def display_products(this):
        print(f'Product name is {this.name}')
        print(f'product price is {this.price}')
'''
mobile = Product()
print(dir(mobile))

mobile.store_products('iphone',55000)
print(mobile.name)
print(mobile.price)
mobile.display_products()

laptop = Product()
laptop.store_products('lenovo',30000)
print(laptop.name)
print(laptop.price)
laptop.display_products()

for i in range(5):
    product = Product()
    product.store_products(input("Enter product name: "),input('Enter product price: '))
    Product.product_lst.append(product) 

for product in Product.product_lst:
    product.display_products()
    print()
'''

class Student:
    """student details of AAA batch"""
    batch = 'AAA-HYD-001'
    def __init__(self):
        self.name = input('Enter the students name:')
        self.age = int(input("Enter your age:"))
        self.place = input("Enter your place:")
    def details(self):
        print(f"student name is {self.name}")
        print(f"student is from {self.place} with age as {self.age} years old") 
        
stud1 = Student()
stud1.details()
'''
stud1 = Students()
print(stud1.batch)
stud1.student_data()
stud1.details()
print(stud1.__dict__)
print(stud1.__doc__)
print(stud1.__class__)
'''