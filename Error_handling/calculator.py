num1 = int(input("enter num1"))
num2 = int(input("enter num2"))

operation = input("select operands + - * / :")
result=0

try:
    if operation=="+":

        result = num2+num1

    elif operation == "-":

        result = num2 - num1 

    elif operation == "*":

        result = num2* num1

    elif operation == "/":

        result = num2/num1

    else:

        print("invalid input")
            
except Exception as e:

    print(e)

else:
    print(result)


