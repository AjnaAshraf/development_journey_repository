for r in range (5,1,-1):

    for sp in range(1,r-1):

        print(" ",end=" ")

    for c in range(1,8):

        if c == 4:

            print(1 ,end=" ")

        elif r==4 or r == 3 or r == 2 or  c == 3 or c ==5 :

            print(2 ,end=" ")

        elif r ==3 or r ==2 or c == 2 or c == 6:
            print(3 ,end=" ")

        elif r == 2 or c ==1 and c==7:
            print(4 ,end=" ")

    print()       

            