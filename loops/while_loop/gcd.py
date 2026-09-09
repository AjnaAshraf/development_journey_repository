"""
gcd 

"""

num1 =  int(input ("enter the number1: "))

num2 = int(input ("enter the number2: "))

i = 1

while i <= min(num1, num2):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1

print("GCD =", gcd)