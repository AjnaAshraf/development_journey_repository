"""
1. **Positive Number – Even or Odd**
   - Check if positive. If yes, check for even/odd. Else, state "Not a positive number."

"""

number = int(input("enter number: "))

if number > 0:

    if number%2 == 0:

        print(number," is a even number")
    
    else:

        print(number," is a odd number")

else:

    print(number," is is not a positive number")
