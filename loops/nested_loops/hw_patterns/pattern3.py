"""  
number increasing pyramid

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

for r in range(1,6):

    for c in range(1,r+1):

        print(c,end=" ")
    
    print()