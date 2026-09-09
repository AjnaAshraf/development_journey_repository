"""
polymorphism => more than one form or many form

    method overloading - same method name but different number of parameters =>this is not supported by python
    method overriding => child class redefines the method that is already defined in the parent class
   

"""

#method overloading  eg:

class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

calc_instance = Calculator()

calc_instance.add(1,2,3,4)# this will work and shows the output
calc_instance.add(1,2,3)# this will not work shows error since python doesnt support overloading 
#it can only remember the last method add() .

