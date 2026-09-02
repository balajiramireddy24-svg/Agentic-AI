# Inheritance 

# super()
'''
class RBI:
    """Parent Class with Major cash"""
    available_cash = 100000000 # class attribute
    @classmethod
    def rbi_cash(cls):
        print(f"RBI has {cls.available_cash}")
class SBI(RBI):
    pass
class HDFC(RBI):
    hdfc_cash=5000000
    @classmethod
    def hd_cash(cls):
        amt = cls.available_cash+cls.hdfc_cash
        print(f"HDFC Cash is {cls.hdfc_cash}")
        print(f"Total cah acessible for Hdfc is {amt}")

a = RBI()
#print(a.available_cash)
#a.rbi_cash()

#sbi = SBI()
#print(dir(sbi))
a.rbi_cash()
h = HDFC()

h.hd_cash()
'''

# same attribute 
'''
class RBI:
    """Parent Class with Major cash"""
    cash = 100000000 # class attribute
    @classmethod
    def rbi_cash(cls):
        print(f"RBI has {RBI.cash}")
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=5000000
    @classmethod
    def hd_cash(cls):
        amt = RBI.cash+HDFC.cash
        print(f"HDFC Cash is {HDFC.cash}")
        print(f"Total cah acessible for Hdfc is {amt}")

a = RBI()
#print(a.available_cash)
#a.rbi_cash()

#sbi = SBI()
#print(dir(sbi))
a.rbi_cash()
h = HDFC()

h.hd_cash()
'''

# Father --> Kid Property
# in this case we will have constructor only in parent class

'''
class Father:
    """Father will have some property`"""
    def __init__(self):
        self.property = 500000
    def fater_property(self):
        print(f"Father Property val is {self.property}")
class Kid(Father):
    #pass
    def __init__(self):
        self.property = 100000
    def kid_property(self):
        print(f"Kid own Property is {self.property}")
        print(f"Final kid Property is {self.property+self.property}")
val = Kid()
print(val.property)
val.fater_property()
val.kid_property()'''

# Super ()
'''
class Father:
    """Father will have some property`"""
    def __init__(self):
        self.property = 5000000
    def fater_property(self):
        print(f"Father Property val is {self.property}")
class Kid(Father):
    #pass
    def __init__(self):
        self.property1 = 100000
        super().__init__()
    def kid_property(self):
        print(f"Kid own Property is {self.property1}")
        print(f"Final kid Property is {self.property1+self.property}")
val = Kid()
print(val.property1)
# print(val.kid_property())  # attribut error
#super 


print(val.property)
val.kid_property()
'''
# calling super clas with arguments
'''
class Father:
    """Father will have some property`"""
    def __init__(self,name,property):
        self.property = property
        self.name = name
    def fater_property(self):
        print(f"Father name is {self.name}, property  is {self.property}")
class Kid(Father):
    #pass
    def __init__(self,name,property1,property):
        self.property1 = property1
        self.name = name
        super().__init__(name,property)
    def kid_property(self):
        print(f"Kid name is {self.name}, Property is {self.property1}")
        print(f"Final kid Property is {self.property+self.property1}")
val = Kid('Rakesh',2300,5000)
val.kid_property()
# 2.
class Father:
    """Father will have some property"""
    def __init__(self, property=100000):
        self.property = property

    def fater_property(self):
        print(f"Father name is {self.name}, property is {self.property}")

class Kid(Father):
    def __init__(self, name, property1, property):
        self.property1 = property1
        self.name = name
        super().__init__(property)

    def kid_property(self):
        print(f"Kid name is {self.name}, Property is {self.property1}")
        print(f"Final kid Property is {self.property + self.property1}")


val = Kid('Rakesh', 2300, 5000)
val.kid_property()

g = Kid("Raki", 5000, 3000)
g.kid_property()
'''



# Area
'''
class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        print(f"Area of Square is {self.x * self.x}")


class Rectangle(Square):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        print(f"Area of rect is {self.x * self.y}")
        super().area()       # IMPORTANT: () after super


x, y = map(float, input("Enter vals: ").split(","))
res = Rectangle(x, y)
res.area()
'''



# whats scenario

'''
class Users:
    def send_message(self):
        print("Sending Message")


class Notifications(Users):
    def notification(self):
        print("Sending Notification")


class PremiumUsers(Notifications):
    def premium(self):
        print("Premium accessing")


u1 = PremiumUsers()

u1.premium()
u1.notification()
u1.send_message()
'''


 # multilevel


class Users:
    def make_calls(self):
        print("Making video calls")


class BusinessUsers(Users):
    def creat_catlog(self):
        print("Products available")


class VerifiedBusinessUsers(BusinessUsers):
    def verification_badge(self):
        print("Blue tick verified")


u1 = VerifiedBusinessUsers()

u1.verification_badge()
u1.creat_catlog()
u1.make_calls()
