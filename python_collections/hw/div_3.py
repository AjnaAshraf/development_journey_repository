"""
2.Create a list and Print elements is divisible by 3.

LIST=[1,4,6,9,12,25,24
"""

lst=[1,4,6,9,12,25,24]

div_by_3 = [num for num in lst if num%3==0]
print(div_by_3)