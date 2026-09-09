"""
* * * * * *     row =6 ,sp =0, col =6
 * * * * *      row =5 ,sp =1, col =5
  * * * *       row =4 ,sp =2, col =4
   * * *        row =3 ,sp =3, col =3
    * *         row =2 ,sp =4, col =2
     *          row =1 ,sp =5, col =1




"""

for r in range(6,0,-1):

    for sp in range(0,(6-r)):

        print(" ",end="")

    for c in range(1,r+1):

        print("* ", end="")
    
    print()