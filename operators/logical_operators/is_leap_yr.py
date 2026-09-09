yr=int(input("enter the year: "))
is_leap_yr= (yr%100 != 0 and yr%4 == 0) or (yr%100 == 0 and yr%400 == 0)
print("is",yr,"leap year: ",is_leap_yr)