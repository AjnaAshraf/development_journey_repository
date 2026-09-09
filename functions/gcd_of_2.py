def gcd_of_2(num1,num2):

    gcd = 1

    for i in range(1,min(num1,num2)+1):

        if num1 % i == 0 and num2 % i == 0:

            gcd = i

    print(gcd)

gcd_of_2(4,8)