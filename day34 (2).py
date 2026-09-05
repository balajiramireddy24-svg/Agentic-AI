'''
OOP -> Encapsulation, Inheritance
'''

# Encapsulation


# useage of Public Attributes
'''
class Users:
    """Useage of Public Attributes """
    def __init__(self,name):
        self.name = name # Public attribute
    def display(self):
        return f"{self.name} is in AAA batch"
print(Users.__doc__)
user1 = Users("jagadeesh boyalla")
print(dir(user1))
print(user1.display())
user1 = Users("JAGADEESH")
print(user1.display())
print(user1.__dict__)
'''
# Protected usage
'''
class Users:
    """Useage of Protected Attributes """
    def __init__(self,name,_otp):
        self.name = name # Public attribute
        self._otp= _otp # Protected Attribute 
    def display(self):
        print(f"{self.name} is in AAA batch")
        print( f"{self._otp} is Otp ")

print(Users.__doc__)
print()
user1 = Users("jagadeesh boyalla",23456)
user1.display()
user1._otp = 34567
print(user1.__dict__)
user1.display() '''

# Private usage
'''
class Users:
    """Useage of Protected, Public,Private Attributes """
    def __init__(self,name,_otp,password):
        self.name = name # Public attribute
        self._otp= _otp # Protected Attribute
        self.__password = password #private
    def display(self):
        print(f"{self.name} is in AAA batch")
        print( f"{self._otp} is Otp ")
        print( f"{self.__password} is Password ")


print(Users.__doc__)
print()
user1 = Users("jagadeesh boyalla",23456,"admin123")
print(user1.name)
print(user1._otp)
#print(user1.__password) print(user1._otp)
#print(user1.password) # Attribute error
print(dir(user1))
print(user1._Users__password) # NameMangling
user1.display()'''

# Acesssing private attribute using getter and setter 
'''
class Users:
    """Useage of Protected, Public,Private Attributes """
    def __init__(self,name,password):
        self.name = name # Public attribute
        self.__password = password #private
    """Acesssing Private attribute  using getter method"""
    def get_password(self):
        return "******"
    # Using Setter Method we want want validates
    def set_password(self,new_password):
        if len(new_password) < 6:
            print(f"Erros are validating the password, enter at leats 6 characters ")
        else:
            self.__password= new_password
            print(f"The password is modify and it is {self.__password}")
user1= Users("jagadeesh","admin123")
print(user1.get_password())
user1.set_password("123") # validate
user1.set_password("qwerty123")
print(user1.__dict__)'''

# getter and setter for otp

'''
class Users:
    """Useage of Protected Attributes """
    def __init__(self,name,_otp):
        self.name = name # Public attribute
        self._otp= _otp # Protected Attribute
     def get_otp(self):
        return self._otp
    def set_otp(self,new_otp):
        if new_otp < 6:
                print(f"Erros are validating the OTP, enter at leats 6 characters ")
        else:
            self._otp= new_otp
            print(f"The password is modify and it is {self._otp}")

print(Users.__doc__)
print()
user1 = Users("jagadeesh boyalla",234567)
print(user1.get_otp())
user1.set_otp(543234)
print(user1.__dict__)
'''



# Inheritance



# Scenario  of usernames creations and update in profile page
'''
class Users:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname+self.lname
user1 = Users("jagadeesh","boyalla")
print(user1.full_name())
class up_user(Users):
    def up_name(self):
        return self.fname.title().strip()+" " + self.lname.title().strip()
user1= up_user("jagadeesh","boyalla")
print(user1.full_name())
print(user1.up_name())

'''



# single inheritence

'''
User --> parent

Update user1  --> child1

Update user2  --> child2

'''



# Whatsapp scenario --> Users, Busiines users (Single)
'''
class Users:
    def send_msg(self):
        print("Sent message")
        
    def voice_call(self):
        print("Sent Voice_call")
    def video_call(self):
        print("Video_call")
    def send_sticker(self):
        print("send a sticker")
class Business(Users):
    def cost_item(self):
        print("The cost of item is")
    def prod_ads(self):
        print("Ads of product is")
u1  = Business()
print(dir(u1))
'''



        
