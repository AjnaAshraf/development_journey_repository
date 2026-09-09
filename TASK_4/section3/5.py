"""
**Water Intake (Liters)**: < 2 (Dehydrated), 2 – 3 (Adequate), > 3 (Excess)


"""

water = int(input("Enter water intake (in liters): "))

if water < 2:

    print("Dehydrated")

elif water <=3:
    print("Adequate")

else:
    print("Excess")