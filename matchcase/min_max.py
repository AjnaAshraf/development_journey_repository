num1 = int(input("enter number 1: " ))
num2 = int(input("enter number 2: "))

option = input("enter option (min/max): ")

match option:

    case "min":
        
        if num1<num2:

            print(" minimum is number 1=> ",num1)

        else:

            print(" minimum is number 2=> ",num2)

    case "max":

        if num1> num2:

            print("maximum is number 1 => ",num1)

        else:

           print("maximum is number 2 => ",num2)

    case _: print("invalid option ")
