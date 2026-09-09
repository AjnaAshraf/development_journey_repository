def is_leap_year(start,stop):

    for year in range(start,stop+1):

        if (year %100==0 and year%400==0 ) or (year%100!=0 and year%4==0):

            print(f"{year} is leap year ")

is_leap_year(2000,2026)
