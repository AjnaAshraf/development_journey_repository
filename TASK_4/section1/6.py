"""

**Student Grading**:
   - Marks ≥ 90: Grade A
   - Marks ≥ 75: Grade B
   - Marks ≥ 50: Grade C
   - Otherwise: Fail

"""

mark = int(input("enter mark: "))

if mark >= 90:
    print("GRADE A")
elif mark >= 75:
    print("GRADE B")
elif  mark >= 50:
    print("GRADE C")
else:
    print("FAILED")