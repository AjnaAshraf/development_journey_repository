"""
Convert 250 minutes into hours and minutes using division and modulus.
"""

total_min=int(input("enter the total minutes:"))

hr=total_min//60
min=total_min%60

print(total_min,"minutes is",hr,"hour and",min,"minutes.")
