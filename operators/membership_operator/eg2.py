#string

p1="ajna"
p2="ajna"

"""
since same value in each variable ie,ajna => same memory location is allocated to the object created 
"""

print(p1==p2)#true
print(p1 is p2)#true

p1_fav=["idly","dosa"]
p2_fav=["idly","dosa"]

"""  since this is not a string python create different objects and assign different memory locations to same values"""

print(p1_fav==p2_fav)#true
print(p1_fav is p2_fav)#false

