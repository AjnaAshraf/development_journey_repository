"""
scenario: reverse number 123 o/p{321}

"""

num = int(input ("enter the number: "))

while (num != 0):

    digit = num % 10

    print(digit)

    num = num // 10

    