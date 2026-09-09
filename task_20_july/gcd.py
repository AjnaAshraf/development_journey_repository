class Gcd:

    def check(self,number1,number2):

        gcd = 1

        minimum = min(number1,number2)
        

        for num in range(2,minimum+1):

            if number1%num == 0 and number2 % num == 0:

                gcd = num

        print(f"gcd of {number1} and {number2} are ",gcd)

gcd_instance=Gcd()
gcd_instance.check(6,8)
gcd_instance.check(4,8)


        

