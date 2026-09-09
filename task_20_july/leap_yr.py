class Leapyear:

    def is_leap(self,year):

        if (year % 100 ==0 and year%400 ==0) or (year%100!=0 and year%4==0):

            return True

        else:

            return False


year_instance = Leapyear()

print(year_instance.is_leap(1994))
print(year_instance.is_leap(2000))
print(year_instance.is_leap(2025))
        
