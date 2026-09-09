def is_fibanocci(num):

    first=0
    second=1
    next = 1

    while (next<=num):

        next = first + second

        if next == num:

            print(num,"is fibanocci number")
            break
            

        first = second
        second = next

    else:

        print(num,"not fibanocci number")

is_fibanocci(24)
is_fibanocci(55)
is_fibanocci(34)