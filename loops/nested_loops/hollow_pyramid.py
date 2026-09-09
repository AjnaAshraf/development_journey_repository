"""
      *             row =6 sp =6 col=1
     * *            row =5 sp =5 col=2
    *   *           row =4 sp =4 col=2
   *     *          row =3 sp =3 col=2
  *       *         row =2 sp =2 col=2
 * * * * * *        row =1 sp =1 col=6

"""


for r in range(1,6):
    for c in range(1,10):
        if r+c == 6 or c-r == 4 or r==5:

            print("*",end=" ")

        else:

            print(" ",end= " ")

    print()
