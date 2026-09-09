"""
    *   
   * *    
  * * *   
 * * * *  
  * * *    
   * *    
    *       

"""


# Upper half
for r in range(1, 5):

    for s in range(4 - r):
        print(" ", end="")

    for c in range(r):
        print("* ", end="")

    print()

# Lower half
for r in range(3, 0, -1):

    for s in range(4 - r):
        print(" ", end="")

    for c in range(r):
        print("* ", end="")

    print()