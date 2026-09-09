class Fact:

    def factorial(self,num):  #3

        factorial = 1

        for i in range(1,num+1):  #1 ,2 ,3

            factorial = factorial * i  # 1,2,6

        print(f" the factorial of {num} is :{factorial}")

fact_inst = Fact()

fact_inst.factorial(3)