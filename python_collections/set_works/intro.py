"""
    set
===========
define {values,values},set()
unordered,so indexing is not supported 
mutable:yes
duplicates_allowed: no
methods:
        add(value) -- add value to the set 
        union---combines both sets without duplicates
        intersectiion ---- takes the common elements in both sets
        difference ---- set_1 diff set b == remove elements of b from set a
        issuperset(set)
        issubset()

"""
st={}   #atleast one value should be present in the curly brackets,otherwise it will be identified as dictionary
print(type(st)) #class dict

st1={1,3,5,7}
print(type(st1))

set = {1,2,3,4,5,3,4,5,2,8}
print(set)

#methods 

set.add(100)
print(set)

set_a={10,20,30,40,50}
set_b={10,20,30,100,200,300}

union_set = set_a.union(set_b)
print("union set: ",union_set)

intersection_set = set_a.intersection(set_b)
print("intersection_set: ",intersection_set)

difference_set = set_a.difference(set_b)
print("difference set: ",difference_set)

difference_set2 = set_b.difference(set_a)
print("difference set",difference_set2)


set_1={10,20,30,40}
set_2={10,20,30,40,100,200,300}

print(set_1.issubset(set_2))
print(set_2.issuperset(set_1))
