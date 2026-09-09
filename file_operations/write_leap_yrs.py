fw = open("file_operations\\leap_years.txt","w")

for yr in range(1800,2027):

    if(yr%100!=0 and yr%4==0) or (yr%100==0 and yr%400==0):

        fw.write(str(yr)+"\n")

