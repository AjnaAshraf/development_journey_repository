"""
define : tp = (10,20,30)
immutable
order preserved 
duplicates allowed
methods:count(value),index(value)
"""

tp=(2,3,4,5,3)
print(type(tp))
print(tp)
print(tp.count(3))
print(tp.index(3))

tp2=(5)#will display <class int>
tp1=(10,)#if only one element is present in the tuple it might me recorded as int so to make it tuple add a comma
print(type(tp1))
print(type(tp2))