# use static and class method but amke sure  free delivery shold be applicable when the price > 30000
#where is develiry charages should v]be zero
# below 30000 should be 60 as per classs varible update  

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
        if self.price <= 0:
            print("Invalid price")

        elif self.free_dev(self.price):
            print("Item:", self.name)
            print("Price:", self.price)
            print("Delivery Charges: 0")
            print("Free Delivery")
            print("Total Price:", self.price)

        else:
            total = self.price + Product.delivery_charges
            print("Item:", self.name)
            print("Price:", self.price)
            print("Delivery Charges:", Product.delivery_charges)
            print("Total Price:", total)

    @staticmethod
    def free_dev(price):
        if price > 30000:
            return True
        elif price == 0:
            return f"Price must be  Greaterthan Zero, {False}" 
        else:
            return False


Product.update_delivery()

name = input("Enter product name: ")
price = int(input("Enter product price: "))

obj1 = Product(name, price)

obj1.display_items()

print("Free Delivery:", obj1.free_dev(price))

print(obj1.__dict__)
