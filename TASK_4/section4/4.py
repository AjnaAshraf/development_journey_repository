"""
**Ice Cream Flavors**
   - Input (1-4): Choose from 1 (Chocolate), 2 (Vanilla), 3 (Strawberry), 4 (Butterscotch).
"""
flavour = int(input(" enter (1-4) => Choose from 1 (Chocolate), 2 (Vanilla), 3 (Strawberry), 4 (Butterscotch): "))

if flavour == 1:
    print("the chosen flavour is chocolate")

elif flavour == 2:
    print("the chosen flavour is vanilla")

elif flavour == 3:
    print("the chosen flavour is stawberry")

elif flavour == 4:
    print("The chosen flavour is Butterscotch")

else:
    print("Invalid choice")