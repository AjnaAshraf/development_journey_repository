x1 = int(input("enter x1 of ponit 1:"))

y1 = int(input("enter y1 of ponit 1:"))

x2 = int(input("enter x2 of point 2:"))

y2 = int(input("enter y2 of point 2:"))

x3 = int(input("enter x3 of point 3:"))

y3 = int(input("enter y3 of point 3:"))

if x1 == x2 or x3 == x2:
    print("cannot find slope because of a vertical line")
else:

    slope_p1_p2 = (y2-y1)/(x2-x1)

    slope_p2_p3 = (y3-y2)/((x3-x2))

    if slope_p1_p2 == slope_p2_p3:

        print("he three points lie on the same line")

    else:
        
        print("the three points doesnot lie on the same line")