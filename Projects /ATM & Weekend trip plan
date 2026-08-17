# Nested Conditions Example

# ATM Withdrawal Scenario

pin = int(input("Enter a PIN: "))
correct_pin = 1888
card_inserted = True
balance = 23000
withdraw = int(input("Enter withdrawal amount: "))
if card_inserted:
     if pin == correct_pin:
         if balance > withdraw:
             print(f"Transaction Successful. New Balance: {balance - withdraw}")
         elif balance <= 0:
             print("Insufficient Balance. Please add money.")
         else:
            print("Transaction Failed. Maintain minimum balance.")
     else:
         print("Invalid PIN")
else:
     print("Account is Deactivated")
Transaction Successful. New Balance: 20557
# Weekend Plan Based on Budget

Budget = int(input("Enter your budget: "))

# Check for invalid budget
if Budget < 0:
    print("Enter Correct Budget")

# Check different budget ranges
elif Budget > 10000:
    print("Plan a Trip")

elif Budget > 5000:
    print("Resort Stay")

elif Budget > 3000:
    print("Movie and Dinner")

elif Budget > 1000:
    print("Cafe and Shopping")

elif Budget > 500:
    print("Street Food and Park Visit")

# Default option
else:
    print("Stay Home")
