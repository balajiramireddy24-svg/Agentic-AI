#Day 12 -- Nested Conditional Statements
#one condition inside another is called as nested conditionals

sales = int(input('input:'))

if sales >= 0:
    if sales > 1000:
        print("Best Seller")
    else:
        print("No Output")
else:
    print("Worst Seller")

#Usecase : ATM Withdrawl Scenario
#check whether card is valid or not

card_details = {'valid_card':True,
                'PIN':9090,
                'balance':1223}

if card_details['valid_card'] == True:
    pin = int(input("Enter PIN:"))
    if pin == card_details['PIN']:
        withdraw_amount = int(input("Enter withdraw amount:"))
        if withdraw_amount <= card_details['balance']:
            print(f'Dispensed Cash {withdraw_amount}')
            card_details['balance'] -= withdraw_amount
            balance_check = input("Do you want to see the remaining balance:? Enter True or False ").lower()
            if balance_check == 'true':
                print("Remaining Balance:", card_details['balance'])
            elif balance_check == 'false':
                print("Remember to take back your card")
        else:
            print("Withdrawal amount exceeding balance amount")
    else:
        print("incorrect PIN number")
else:
    print("Your Card is invalid")

#weekend planner

budget = int(input("input:"))
if budget >= 10000 * 0.99:
    print('Plan: Trip')
elif budget >= 5000 * 0.99:
    print('Plan: Resort Stay')
elif budget >= 3000 * 0.99:
    print('Plan: Movie and Dinner')
elif budget >= 1000 * 0.99:
    print('Plan: Cafe and Shopping')
elif budget >= 500 * 0.99:
    print('Plan: street Food and Park Visit')
else:
    print('Plan: Stay Home')
