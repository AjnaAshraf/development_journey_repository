

def last_divisor(num):

    for i in range(1,num):

        if num % i == 0:

            gcd = i

    print(gcd)


last_divisor(8)
last_divisor(9)

