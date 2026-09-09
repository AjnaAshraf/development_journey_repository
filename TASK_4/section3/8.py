"""
 **Urine Color (1-8)**: 1 – 3 (Well Hydrated), 4 – 6 (Mild Dehydration), 7 – 8 (Severe)

"""

urine_color = int(input("Enter urine color level (1-8): "))

if urine_color < 1 or urine_color > 8:

    print("Invalid input")

if urine_color<= 3:
    
    print("Well Hydrated")
elif urine_color <= 6:
    print("Mild Dehydration")
else:
    print("Severe")