fw = open("file_operations\\prime_numbers.txt","w")

for num in range(50,101):

    for n in range(2,num):

        if num%n==0:

           break

    else:

        fw.write(str(num)+"\n")

print("write completed")
