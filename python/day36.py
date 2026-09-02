'''
Inheritance -->Hierarchical  Inheritance,Hybrid Inheritance

Hierarchical Inheritance   -->It is type of Inheritance where multiple child classes inherit properites
from single parent (base) class

class parent :
    pass
class child(parent):
    pass
class child2(parent):
    pass
class child3(parent):
    pass
class child4(parent):
    pass...
    .........
..........

#Whatapps scenario

class User:
    """User class witrh message Properties """
    def send_message(self):
        print(f'Sending Messages')
class PersonalUser(User):
    """Personal User class inheriting from User class """
    def status_update(self):
        print(f' Status Update only for contacts ')
class BusinessUser(User):
    """Business User"""
    def create_catalog(self):
        print(f' Catalog Ceration is possbile ')
    def status_update(self):
        print(f' Status Update only for contacts ')
class VerifiedBusinessUser(User):
    """verified User"""
    def premium_access(self):
        print(f' Blue Tick added ,with premium features loaded')

user1=User()
user1.send_message()
user2=PersonalUser()
user2.send_message()
user2.status_update()
user3=BusinessUser()
user3.create_catalog()
user3.send_message()
user3.status_update()

#Hybride Inheritance --> it is a type inheritance in which one or more than one type or Inheritance 
class User:
    """User class with voice calls"""
    def voice_call (self):
        print(f'Making Voice calls')
        def video_call(self):
            print(f'Making Vedio Call')
class Notification(User):
    """sender Notification """
    def noyify(self):
        print('sending Notification')
class BusinessUser:
    """Business user access"""
    def catalog(slef):
        print(f' catalog is update ')
class PremiumBusinessUser(BusinessUser,Notification):
    """Premium Content"""
    def premium_access(self):
        print(f' Blue Tick Verification and Reach Access')
u1=BusinessUser()
u1.catalog()
u2=PremiumBusinessUser()
u2.premium_access()

#Polymorphism --->feature of OOP
#Ploy   -->many
#morph -->forms

#Method Overloading  --->Method with defaults arguments,Method 
#Method Overriding
#Operator Overloading -->__add__,__str__


#Hotstar -->FreeUser ,Premium User,Adavence Premium User

class HotStar:
    """Simple example to Understand polymorphism """
    def watch(self):
        print(f'Welcome to HotStar Home Page....Content Loading')
    def watch(self,movie ):
        self.movie =movie 
        print(f'Loaded HotStar  Watching  Movie {self.movie}')
user=HotStar()
user.watch("OG")
#user.watch()
'''
#Method Overloading with default arguments :
class HotStar:
    """MethodOver Loading with default arguments """
    def watch(slef,movie=None):
        if   movie==None :
            print(f' Welcome to HotStar')
        else:
            print(f'Watching {movie }')
   
user=HotStar()
user.watch()
user.watch("OG")
user.watch("Leo")


class HotStar:
    """MethodOver Loading with default arguments """
    def add_to_watchlist(self,*movie ):
        print(f' Movies Added ')
        for movies in movie :
            print(f'{self.movies}')
user=HotStar()
user.add_to_watchlist('Leo','OG','Salaar','Sahoo')
        


#Method overloading -->

class HotStar:
    """checking the type of arguments  Usage """
    def Movies_list(self,content):
        if isinstance(self ,str):
            print(f' Watching {content}')
        elif isinstance (content,list):
            print(f'Movies Added ')
            for movie in content:
                print(movie )
user=HotStar()
user.movies_list("OG")
user.movies_list(['leo','og','syp'])








 
