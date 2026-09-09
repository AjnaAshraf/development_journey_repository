def sum_of_n(start,stop):

    sum = 0

    for i in range(start,stop+1):

        sum = sum + i

    print(f"the sume of numbers from {start} to {stop} is: {sum}")

sum_of_n(1,8)

sum_of_n(50,100)