"""
1. Blood Sugar
- < 100: Normal
- 100 – 125: Prediabetes
- ≥ 126: Diabetes

"""

sugar_level = int(input("enter your sugar level: "))

if sugar_level < 100:
    print(" normal")

elif sugar_level >= 100 and sugar_level <=125:
    print(" prediabetes")

else:
    print("diabetes")