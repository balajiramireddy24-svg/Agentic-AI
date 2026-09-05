#Day 32 --> Private attributes and accessing them


#usage of public attributes
'''
class Users:
    """Usage of public attributes"""
    def __init__(self,name):
        self.name = name #public attribute

    def display(self):
        return f"{self.name} is in AAA batch"

user1 = Users('Saketh kallepu')
print(user1.__dict__)
print(user1.display())
user1 = Users('Saketh')
print(user1.display())
print(user1.__dict__)
'''
'''
class Users:
    """Usage of Protected Attributes"""
    def __init__(self,name,_otp):
        self.name = name
        self._otp = _otp

    def display(self):
        print(f"{self.name} is in AAA Batch")
        print(f"otp is {self._otp}")

user1 = Users("Agent",234567)
print(user1._otp)
print(user1.__dict__)
user1.display()
user1._otp = 123456
print(user1.__dict__)
user1.display()
'''
'''
class Users:
    """Usage of Protected Attributes"""
    def __init__(self,name,_otp,password):
        self.name = name #public attribute
        self._otp = _otp #Protected attribute --> uses single underscore
        self.__password = password #private attribute

    def display(self):
        print(f"{self.name} is in AAA Batch")
        print(f"otp is {self._otp}")
        print(f"logged in with {self.__password}")

user1 = Users('pavan',123456,'admin123')
print(user1.name)
print(user1._otp)
#print(user1.password) #attribute error --> because is password is private attribute and is not allowed to be accessible to everyone
user1.display()
print(user1._Users__password) #Name Mangling
'''
'''
#Accessing Private Attributes using getter and setter methods
class Users:
    """Usage of Protected Attributes"""
    def __init__(self,name,_otp,password):
        self.name = name #public attribute
        self._otp = _otp #protected attribute
        self.__password = password #private attribute
    #Accessing Private attribute using getter method
    def get_password(self):
        return self.__password #here we are accessing
    def set_password(self,new_password):
        if len(new_password) < 6:
            print(f"Password should be minimum of 6 characters")
        else:
            self.__password = new_password
            print(f"Your Password has been set to '{self.__password}'")
    def get_otp(self):
        return self._otp
    def set_otp(self,new_otp):
        self._otp = new_otp
        print(f"Your new otp is {self._otp}")

user1 = Users('Pavan','123456','admin123')
print(user1.get_password())
print(user1.set_password('python'))
print(user1.get_otp())
user1.set_otp('098765')
'''

#Inheritence --> One of the key principles in OOP
#which mainly focuses on acquiring the properties from base class (parent class) to derived class(Child class)
#There are four types of class inheritences --> Single, Multiple, Multilevel, Hybrid
'''
Syntax

class Parent:
    statement(s)...
    ......
    
class child(Parent):
    statement(s)...
    ......
'''
#Scenario of Usernames creation and Updation in Profile Page
#Single Inheritence --> Users --> Parent class, Update_User --> child class
'''
class Users:
    """User Details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname +" "+ self.lname

#user1 = Users('Pavan','Pusapati')
#print(user1.full_name())

class Update_Users(Users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()

user1 = Update_Users('pavan','pusapati')
print(user1.full_name())
print(user1.update_name())
'''

class Users:
    def __init__(self,name):
        self.name = name
    def message(self):
        return "Message Sent"
    def send_photo(self):
        return "Photo Sent"
    def send_video(self):
        return "Video Sent"

class Business_Users(Users):
    def display_catalog(self):
        return "Display Catalog"

user1 = Business_Users("Pavan")
print(user1.message())
print(user1.display_catalog())