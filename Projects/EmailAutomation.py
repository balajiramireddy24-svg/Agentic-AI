import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "loyola.pavan.74@gmail.com"
password = "hhvb zljw pelr asjb"

recipients = [
    "bestfriendpavan2003@gmail.com",
    "pavanpusapati07@gmail.com",
    "ppusapat@student.gitam.edu"
]

subject = "Test Mail"
message = "This is a Test mail, Please Ignore it"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

print("Login Successful")

for recipient in recipients:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server.sendmail(sender, recipient, msg.as_string())

server.quit()
print("All emails sent successfully.")