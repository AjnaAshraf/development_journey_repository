"""
q2)scenario : factorial of a number 4 ---> o/p {24}
"""

num = int(input ("enter the number whose factorial is to be found: "))
factorial = 1
i =1

while (i<= num):

    factorial = factorial * i

    i = i + 1

print(f"factorial of {num} = {factorial}")