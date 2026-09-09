"""
20. Price increases from 1200 to 1500. Find increase amount and percentage.
"""

op=int(input("enter the original price: "))
np=int(input("enter the new price: "))

increased_amount=np-op
percentage=(increased_amount/op)*100

print("the increased amount is: ",increased_amount)
print("the percentage increased is: ",percentage,"%")
