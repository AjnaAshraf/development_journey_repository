# w a p to create a new collection that contain only prime numbers

arr = [3,4,7,9,19,5,13,23,12]

prime_numbers = list()

for num in arr:

    for i in range(2,num):

        if num%i == 0:
            break

    else:

        prime_numbers.append(num)

print(prime_numbers)