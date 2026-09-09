"""
**Exercise (Min)**: < 30 (Insufficient), 30 – 60 (Good), > 60 (Intense)


"""

exercise = int(input("Enter exercise time (in minutes): "))

if exercise < 30:
    print("Insufficient")
elif exercise <= 60:
    print("Good")
else:
    print("Intense")