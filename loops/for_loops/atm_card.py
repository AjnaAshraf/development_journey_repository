real_pin = 1234

for attempt in range(1,4):

    pin = int(input("enter the 4 digit pin: "))

    if pin == real_pin:

        print("succesfully unlocked")
        break

else:

    print("atm card blocked")

    