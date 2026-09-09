"""
 **Driving License Eligibility**
   - Age ≥ 18: Ask if test passed (yes/no).
   - Yes: "License Approved" | No: "Test not cleared."
   - Age < 18: "Not eligible due to age."

"""

age = int(input("enter age: "))

if age >= 18:

    test = input("did you pass the test (yes/no): ")

    if test == "yes":

        print("License Approved")

    else:

        print("Test not cleared")

else:

    print("Not eligible due to age")
    
    
     