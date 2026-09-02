#Day 24 --> sending automated email using attachment, datetime module and string formatting
'''
import os
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

frommail = 'loyola.pavan.74@gmail.com'
tomail = 'bestfriendpavan2003@gmail.com'
subject = 'Email automation using python - single user with attachment'
app_password = 'hhvb zljw pelr asjb'
body = "in this project we will understand how python can be useful in real world applications"
attach = 'day01.py'
msg = MIMEMultipart()

msg['From'] = frommail
msg['To'] = tomail
msg['Subject'] = subject
msg.attach(MIMEText(body))

part = MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(frommail,app_password)
server.sendmail(frommail,tomail,msg.as_string())
print("Mail Sent")
server.quit()
'''

'''
datetime --> time,date module for time and date functionalities
'''
import datetime

from datetime import datetime

a = datetime.now()
print(a)
print(type(a))

print(a.date())

print(f'today is {a.day}-{a.month}-{a.year}')

g = datetime.today()
h = g.weekday()
k = g.isoweekday()

l = datetime.time(g)
print(l)

#string Formatting --> convert datetime to string
print(g.strftime('%w')) #number of days int his month
print(g.strftime('%m'))

#