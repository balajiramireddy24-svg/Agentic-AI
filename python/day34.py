'''
class Users:
    """Useage of protected Attributes """
    def  __init__(self,name,_otp):
        self.name =name
        #Public Atttribute s
        self._otp   #Protected Attributes

    def display(slef):
        print(f'{self.name} is in AAA batch')
        print(f'   OTP is {self._otp}')




        

class Users:
    """Useage of protected & private Attributes """
    def  __init__(self,name,_otp,password):
        self.name =name#Public Atttribute s
        self._otp   #Protected Attributes
        self._password =password    #Private Attribute

    def display(slef):
        print(f'{self.name} is in AAA batch')
        print(f'   OTP is {self._otp}')
        print(f' Logged in with {self._password}')
user1 = Users("Balaji",934921,"admin75")
print(user1. name )
print(user1._otp)
#print(user1.password)    #Attribute Error 
print(dir(user1))
print(user1._users_password)       #NameMangLing
user1.display()

#Accessing private Attribute using getter and setter Methods ...

class Users:
        """Useage of protected & private Attributes """
        def  __init__(self,name,password):
            self.name =name#Public Atttribute
            self._password =password    #Private Attribute

            #Accessing private attribute using getter method
        def  get_password(self) :
                 return    "******"     #Here we are accessing

            #Using setter Method we want to have validations
        def set_password(self,new_password)  :
            if len(new_password )   <  6:
                print(f'Error in validating the password,enter at least 6 characters')
            else:
                self._password = new_password
                print(f' The password is modified and it is {self._password}')
user1 = Users("Balaji","admin123")
print(user1.get_password())
print(user1.__dict__)
user1.set_password("123")
user1.set_password ("qwerty123")
print(user1.__dict__)

#getter () and settter () otp
class Users:
        """Useage of protected & private Attributes """
        def  __init__(self,name,_otp):
            self.name =name#Public Atttribute
            self._otp =_otp    #Private Attribute
             #Accessing private attribute using getter method
        def  get_otp(self) :
                 return    "******"     #Here we are accessing

            #Using setter Method we want to have validations
        def set_otp(self,new_otp)  :
            if len(new_otp )   <  6:
                print(f'Error in validating the otp,enter at least 6 characters')
            else:
                self._otp = new_otp
                print(f' The OTP is modified and it is {self._otp}')
user1 = Users("Balaji",564585)
print(user1.__doc__)
print(user1.__dict__)
user1.set_password (123456)
print(user1.__dict__)

class Users:
        """Useage of Protected Attributes """
        def _init_(self,name,_otp):
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
user1 = Users("Balaji",234567)
print(user1.get_otp())
user1.set_otp(543234)
print(user1._dict_)

'''
#Inheritance   -->One of the principles in OOP ,which mainly focuse on
#acquring the properties from base class (parent class)
#to dervied class(child class)
'''


Syntax for Inheritance :
Class Parent:
        statement(s).....
        ............
Class child(parent):
            Statement(s)........
            .......
'''
#Single Inheritance ,Multiple Inheritance ,Multilevel Inheritance ,Hybrid Inheritance

#Scenarios of Usernames creation and Updation in profile page
'''
class Users :
    """user details """
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name (self ):
        return self.fname+self.lname
#user1=Users("Balaji","Ramireddy")
#print(user1.full_name())
class Update_Users(Users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
user1 =Update_Users("balaji","ramireddy")
print(user1.full_name ())
print(user1.update_name())
'''
#single Inheritance
'''
Users   --->parent

Update User1   (Users)    --->chid1

Update User2 (Users)   -->child2
'''

#Whatsapp Scenario   _-->Users,Business Users(single Inheritance)
class Msg:
    def send_msg(self):
        print("sent Message")
    def vioce_call(self):
        print("Making a Voice Call")
    def video_call(self):
        print("Making a video Call")
    def send_sticker(slef):
        print("Sent Sticker ")
