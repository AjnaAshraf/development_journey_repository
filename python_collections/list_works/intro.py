#expense of first 6 months

expenses = [12000,15000,17000,11000,18000,14000]

print(expenses[3])
march_expense=expenses[2]
print(march_expense)

#update jan month expense as 15000

expenses[0]=15000

print(expenses)


#display all expenses one by one

print("================using index=============")

for i in range(0,len(expenses)):

    print(expenses[i])

print("================Not using index=============")

for amount in expenses:

    print(amount)
