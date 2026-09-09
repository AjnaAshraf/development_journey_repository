"""
5. **Ticket Fare**
   - Age < 5: Free
   - Age 5 – 18: ₹10
   - Age 19 – 60: ₹20
   - Age > 60: ₹15

"""

age = int(input("enter age: "))

if age < 5:
    print("ticket is free")

elif age>=5 and age<19:
    print("ticket fare is ₹10")

elif age>=19 and age<61:
    print("ticket fare is ₹20 ")

else:
    print("ticket fare is ₹15 ")