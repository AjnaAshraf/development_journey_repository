"""

      *             row =6 sp =6 col=1
     * *            row =5 sp =5 col=2
    * * *           row =4 sp =4 col=3
   * * * *          row =3 sp =3 col=4
  * * * * *         row =2 sp =2 col=5
 * * * * * *        row =1 sp =1 col=6


"""

for r in range(6,1,-1):

    for sp in range(1,r):

        print(" ", end = "")

    for c in range(1,(7-r)+1):

        print("* ", end = "")

    print()
