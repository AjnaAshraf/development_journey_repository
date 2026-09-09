"""
 **BMI**: < 18.5 (Underweight), 18.5 – 24.9 (Normal), 25 – 29.9 (Overweight), ≥ 30 (Obese)


"""

height_in_cm=int(input("enter the height in cm: "))
weight_in_kg=int(input("enter the weight in kg: "))

height_in_metre=height_in_cm/100
bmi=weight_in_kg/height_in_metre**2

print("the BMI is: ",bmi)

if bmi< 18.5: print(" UNDER WEIGHT")

elif bmi>=18.5 and bmi<=24.9: print(" NORMAL")

elif bmi>=25 and bmi<=29.9: print(" OVER WEIGHT")

else:
    print("obese ")
