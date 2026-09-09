def fibanocci(num):

    first = 0
    second = 1
    print(first)
    print(second)

    for i in range(1,num-1):

        next = first + second
        print(next)
        first = second
        second = next
    
fibanocci(10)