

"""
   1       r=5 sp=3 1
  2 2      r=4 sp=2 2
 3 3 3     r=3 sp=1 3
4 4 4 4    r=2 sp=0 4



"""
num = 1
for r in range(5,1,-1):

    for sp in range(1,r-1):

        print(" ",end="")

    for c in range(1,(6-r)+1):

        print(num,end = " ")
    
    print()
    
    num = num+1

