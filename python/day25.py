#Day 25 --> datetime objects,pyqrcode module, rock,paper and scissor game with random module
import datetime
'''
b = datetime(2026,8,4)
print(b)
print(type(b))

c = datetime(day=16,month=9,year=2026,hour = 10,minute=30,second=24,microsecond = 23)
print(c)

#accept input from user --> convert to datetime object
#return the string format with date

day,month,year = map(int,input().split())
d = datetime.datetime(year,month,day)
print(d)
print(f'Today is {d.strftime("%A")}')
print(f'today is {d.strftime("%B")}')
'''

#strptime() --> stringpointoftime --> datetime --> str format
'''
from datetime import datetime,timedelta

f = datetime.now()
print(f)

print(type(f))
d_obj = datetime.strptime("1996-12-26","%Y-%m-%d")
print(d_obj)
print(d_obj.strftime("It is %A"))

diff = timedelta(days = 5,hours = 10)
print(diff)
print(f + diff)

print(f + timedelta(hours=5,minutes=30))
d = f + timedelta(hours=5,minutes=30)
print(d)
print(f'future date is {d + timedelta(days=5,hours=10)}')
'''
'''
import time
print(dir(time))
print(time.tzname)
print(time.ctime())
print(time.localtime())

t_obj = time.localtime()
y = t_obj.tm_year
month = t_obj.tm_mon
day = t_obj.tm_mday
print(f"Date is {day}-{month}-{y}")
'''
'''
import random

count1 = 0
count2 = 0

while  count1 < 3 and count2 < 3:

    player1 = input("Enter from [rock,paper,scissor]:").lower().strip()
    player2 = random.choice(['rock','paper','scissor'])

    if player1 == 'paper' and player2 == 'rock':
        print('player 1 wins')
        count1 += 1
    elif player1 == 'scissor' and player2 == 'paper':
        print('player 1 wins')
        count1 += 1
    elif player1 == 'rock' and player2 == 'scissor':
        print('player 1 wins')
        count1 += 1
    elif player1 == player2:
        print("Tie")
    else:
        print("player 2 wins")
        count2 += 1
    print(f"player1: {count1}")
    print(f"player2: {count2}")
'''

#py qr code

import pyqrcode,png
link = "https://www.linkedin.com/in/pavanpusapati/"
qr = pyqrcode.create(link)
print(qr)
qr.png('myqr.png',scale=15)
