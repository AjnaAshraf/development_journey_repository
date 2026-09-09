
num1 = int(input("enter number 1: "))

num2 = int(input("enter number 2: "))

option = (input("choose your operation: (+,-,*,/) : "))

match option:

    case "+":

        print("result of operation is ",num1,"+",num2,": ",num1+num2)

    case "-":

        print("result of operation is ",num1,"-",num2,": ",num1-num2)

    case "*":

        print("result of operation is ",num1,"*",num2,": ",num1*num2)

    case "/":

        print("result of operation is ",num1,"/",num2,": ",num1/num2)

    case  _:

        print(" INVALID INPUT ")


