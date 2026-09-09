#sales of first 6 months

sale = [100000,90000,110000,115000,100000,1160000]

march_months_sale=sale[2]
print("march_months_sale",march_months_sale)

print("=================================")

# update may month sale as 105000

sale[4]=105000
print(sale)


print("=================================")

#display all sales using index

for i in range(0,len(sale)):

    print(sale[i])
print("=================================")
#display sale>100000

for i in range(0,len(sale)):

    if sale[i]>100000:

        print(sale[i])

    """or """

    """
    
    for amount in expenses:
    
    if amount>100000:

        print(amount)
    
    
    """