def is_armstrong(number):

    sum = 0
    original = number
    count = len(str(number))

    while (number!=0):

        digit = number%10
        sum = sum + (digit**count)
        number = number // 10

    if sum == original:

        print(True)

    else:

        print(False)

is_armstrong(1634)
    



