
"""

✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"
"""

db_pin = 123456

db_balance = 2345678

pin = int(input("enter pin: "))

if pin == db_pin:

    amount = int(input("enter the amount to be withdrawn: "))

    if amount <= db_balance:
        
        print(" Withdrawal successful ")
    
    else:

        print( "Insufficient balance")

else:

    print("Incorrect PIN")
