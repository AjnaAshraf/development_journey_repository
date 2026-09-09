"""
**Cholesterol**: < 200 (Desirable), 200 – 239 (Borderline), ≥ 240 (High)


"""

cholesterol = int(input("Enter cholesterol level: "))

if cholesterol < 200:

    print("Desirable")

elif cholesterol < 240:

    print("Borderline")

else:
    
    print("High")