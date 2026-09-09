"""
list methods
============
ADD
    1.append(object)
    2.insert(index,object)

REMOVE

    3.pop(index) #by default index is assigned as -1
    4.remove(value) #removes the first ocuurance of the value from list

5.index(value) returns index position of first occurance of value
6.count(value) returns the frequency of occurance of value
7.reverse() reverse the list
8.sort() alphabetic ascending order,numerical ascending order
9.copy() creates another object of the same list
"""


#append(object)---->appends object at the end of the list

colors = ["red","green","violet","yellow","purple"]

colors.append("white")

#print(colors)

#insert(index,objects)-----> add object at a specified index

colors.insert(2,"orange")

#print(colors)

# pop(index) #by default index is assigned as -1
#syntax : pop(index)

colors.pop()
print(colors)
colors.pop(0)
print(colors)

# remove(object) #removes the first ocuurance of the value
colors.remove("orange")
print(colors)


#index(value) returns index position of first occurance of value

print(colors.index("violet"))

#.count(value) returns the frequency of occurance of value

print(colors.count("green"))
print(colors.count("cyan"))

#reverse()

colors.reverse()
print(colors)

#8.sort() alphabetic ascending order,numerical ascending order

colors.sort(reverse=True)# for descending order
print(colors)

#9.copy() creates another onject of the same list

hiba_fav = ["mandi","peri peri mandi","pakisthani mandi","Honey chilli mandi"]
anjali_fav = hiba_fav.copy()
anjali_fav[1]="porotta"
print(anjali_fav)