def factorial(number):

    result = 1

    for i in range(1,number+1):

        result =  result * i

    print(f"factorial of {number} is: {result}") 

factorial(4)
factorial(5)
