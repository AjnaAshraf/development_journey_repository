"""

# 7. Daily Steps
- < 5000: Sedentary
- 5000 – 9999: Moderately Active
- ≥ 10000: Active

"""


steps = int(input("Enter daily steps: "))

if steps < 5000:
    print("Sedentary")

elif steps < 10000:
    print("Moderately Active")
    
else:
    print("Active")