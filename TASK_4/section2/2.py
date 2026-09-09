"""
2. Blood Pressure (Systolic)
- < 120: Normal
- 120 – 129: Elevated
- 130 – 139: High BP Stage 1
- ≥ 140: High BP Stage 2

"""


bp = int(input("Enter systolic blood pressure: "))

if bp < 120:
    print("Normal")
elif bp < 130:
    print("Elevated")
elif bp < 140:
    print("High BP Stage 1")
else:
    print("High BP Stage 2")