"""
q5) write a program to print least +ve missing number 

     arr=[1,2,4,5]
     o/p => 3

     eg2:
    arr=[1,3,4,5]
     o/p => 2
"""

arr1=[1,3,4,5,7,2]
arr=sorted(arr1)

for num in range(0,len(arr)):

    if arr[num] != num+1:
        print(num+1)
        break
