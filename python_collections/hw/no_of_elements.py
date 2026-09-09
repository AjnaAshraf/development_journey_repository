"""
.Find the no of elements in a list.
"""

lst=[1,4,6,9,12,25,24,-5]

print(len(lst))

# Find the largest element in a list.

print("largest= ",max(lst))

# 5.Find the smallest element in a list.

print("smallest= ",min(lst))

# 6.Calculate the sum of all elements in a list.

print("sum of lst = ",sum(lst))


# 7.Calculate the average of the numbers in a list.
avg=sum(lst)/len(lst)
print("avg of lst = ",avg)

# 8.Find all even numbers in a list.

even = [n for n in lst if n%2==0]
print("evens=",even)

# 9.Find all odd numbers in a list.

odd = [n for n in lst if n%2!=0]
print("odds =",odd)

# 10.Print all numbers greater than 50 from a list.

gt_than_50 = [n for n in lst if n>50]
print("numbers greater than 50 =",gt_than_50)

# 11.Print all numbers less than 20 from a list.
ls_th_20 = [n for n in lst if n<20]
print("numbers less than 20 =",ls_th_20)

# 12.Find all prime numbers in a list.
lst1=[1,4,6,9,12,25,24,7]
for num in lst1:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break

        else:
            print(num)


# 13.Find all negative numbers in a list.

neg = [n for n in lst if n<0]
print(neg)

#14.Create a list [10, 20, 30, 40, 50] and change the value at index 1 to 100

lstt = [10, 20, 30, 40, 50]

lstt[1]=100
print(lstt)

# Given numbers = [5, 10, 15, 20], replace the last element with 50.
numbers = [5, 10, 15, 20]
numbers[-1]=50
print(numbers)

# 16.Given fruits = ["Apple", "Banana", "Orange"], replace "Banana" with "Mango".

fruits = ["Apple", "Banana", "Orange"]

fruits = ["Mango" if fruit == "Banana" else fruit for fruit in fruits]
print(fruits)

# 17.Create a list [1, 2, 3, 4, 5] and update the element at index 3 to 100.
lst2= [1, 2, 3, 4, 5]
lst2[3]=100
print(lst2)
# 18.Given colors = ["Red", "Blue", "Green"], change the first color to "Yellow".
colors = ["Red", "Blue", "Green"]
colors[0]="Yellow"
print(colors)
# 19.Given items = ["Pen", "Book", "Bag"], replace the item at index 2 with "Laptop"

items = ["Pen", "Book", "Bag"]
items[2]="Laptop"
print(items)