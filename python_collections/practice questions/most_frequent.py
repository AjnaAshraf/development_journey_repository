"""
q4)write a program to print most frequent  number

     arr=[10,1,15,16,11,10,12,11,12,18,12]
    
    o/p => 12
"""

arr=[10,1,15,16,11,10,12,11,12,18,12,1,1,1,1,1,1]

# count=0

# for num in arr:

#     counted = arr.count(num)
#     if counted>count:
#         count = counted
#         number = num

# print(number)

max_frequency=arr[0]

for num in arr:

    if arr.count(num)>arr.count(max_frequency):

        max_frequency=num

print(max_frequency)
    

