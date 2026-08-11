#Day 14 --> while loop
#while loop --> checks until and unless the given condition is satisfied

'''
syntax:

while condition:
    statement(s)....
    .....

'''

#sample usage to understand while
'''
count = 5
while count >= 1:
    print(count)
    count -= 1
'''

#asking the user until he gives correct password
#giving the user 3 tries to enter the correct password
'''
password = input("Enter the correct Password:")
checker = 'admin'
count = 1
while password != checker:
    print("Incorrect password, please enter again")
    password = input("Enter the correct password:")
    count += 1
    if count == 3:
        print("Account Freeze")
        break
else:
    print("Login Successful")
'''

#for with else,while with else --> else will be executed only when loop is completely done
#search for a product in the store

'''
store = ['mobile','laptop','watch','charger']
search = input("Enter the search item:").lower()

for item in store:
    if search == item:
        print(f"{search} is available in the store")
        break
else:
    print(f"{search} is not present in the store")
'''

#task
#pin verification , user should be given three chances to type the correct pin
#if 3 wrong pins are entered then the account gets locked for 24 hours
#push it to github and linkedin post

#break,continue,pass --> jumping statements
#break --> it basically skips the current iteration and gets back to the next iteration
#continue --> it basically skips the current iteration and gets back to the next iteration

'''
for i in "codegnan":
    if i == "g":
        continue
    print(i)
'''

#pass --> it is generally used as a placeholder (to have a syntax match)

for i in range(10):
    pass
    print('hi')