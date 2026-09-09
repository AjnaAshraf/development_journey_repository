num=int(input("enter the year: "))
if num%100!=0 and num%4==0:
    print("given year is not divisible by 100 and is divisible by 4.")
else:
    print("dont satisfy the condition")
