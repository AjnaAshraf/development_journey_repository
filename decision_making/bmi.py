height_in_cm=int(input("enter the height in cm: "))
weight_in_kg=int(input("enter the weight in kg: "))

height_in_metre=height_in_cm/100
bmi=weight_in_kg/height_in_metre**2

print("the BMI is: ",bmi)

if bmi<=19: print(" UNDER WEIGHT")

elif bmi>19 and bmi<=25: print(" NORMAL")

elif bmi>25 and bmi<=30: print(" OVER WEIGHT")

else:
    print("obese ")
