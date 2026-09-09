angle_1 = int(input("enter angle 1: "))

angle_2 = int(input("enter angle 2: "))

angle_3 = int(input("enter angle 3: "))

sum_angle = angle_1 + angle_2 + angle_3

if (angle_1>0 and angle_2>0 and angle_3>0): 

    if sum_angle == 180:

        print("it is a triangle ")

    else:

        print(" it cannot form a triangle")
else:

    print("the angles should be greater than zero ")




