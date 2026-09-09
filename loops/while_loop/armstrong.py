num = int(input ("enter the number: "))

original = num

sum = 0

count = len(str(num))

while (num != 0):

    digit = num % 10

    sum = sum + digit ** count

    num = num // 10

if sum == original:

    print(f"{original} is armstrong")

else:

    print(f"{original} is not armstrong")