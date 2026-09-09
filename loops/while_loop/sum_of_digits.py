num = int(input ("enter the number: "))

sum = 0

while(num != 0):

    digit = num % 10

    sum = sum + digit

    num = num // 10

print(f"the sum of digits of number is {sum}")