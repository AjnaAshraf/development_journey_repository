"""
**Exam Marks – Distinction**
   - Marks ≥ 40: Pass.
   - Marks ≥ 90: Distinction.
   - Else: Fail.

"""

marks = int(input("enter mark: "))


if marks >=90:
    print(" Distinction")

elif marks >=40:
    print("pass")
    
else:
    print("Fail")
