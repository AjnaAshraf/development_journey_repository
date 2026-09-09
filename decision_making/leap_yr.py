yr=int(input("enter the year: "))
if (yr%100 != 0 and yr%4 == 0) or (yr%100 == 0 and yr%400 == 0):
    print("the year is leap year")
else:
    print("the year is not leap year")