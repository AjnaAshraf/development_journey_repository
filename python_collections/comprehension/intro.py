"""
comprehension is easy way for creating a collection from sequence

syntax:

list _compre = [return_value iteration condition]
set _compre = {value iteration condition}
dict _compre = {k:v iteration condition}

"""
arr = [2,3,4,5,6,7]
squares = [num**2 for num in arr]
cubes = [num**3 for num in arr]
add_ten = [num+10 for num in arr]

print("squares: ",squares)
print("cubes: ",cubes)
print("10 added to arr: ",add_ten)

evens = [num for num in arr if num%2==0]
odds = [num for num in arr if num%2!=0]
num_gt_five = [num for num in arr if num>5]

print("evens: ",evens)
print("odds: ",odds)
print("numbers greater than 5: ",num_gt_five)