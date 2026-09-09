"""
 **Age Group**: < 13 (Child), 13 – 19 (Teen), 20 – 59 (Adult), ≥ 60 (Senior)


"""

age = int(input("enter age: "))

if age <13:
    print("child")

elif age>=13 and age<20:
    print("teen")

elif age>19 and age<60:
    print("adult")

else:
    print("senior")













