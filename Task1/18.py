"""
18. A train travels 320 km in 4 hours. Find speed and distance in 7 hours.

"""

d1=int(input("enter the distance travelled "))
t1=int(input("enter the time taken "))
speed=d1/t1

print("The speed is:",speed, "km/hour")
t2=int(input("enter the new time"))
d=speed*t2
print("the distance travelled in",t2,"hours is: ",d,"km")