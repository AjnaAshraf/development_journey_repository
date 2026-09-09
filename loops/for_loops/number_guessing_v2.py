from random import randint

secret_number = randint(1,10)

for attempt in range(1,6):

    num = int(input("guess the number......"))


    if num < secret_number:

        print("too low")

    elif num > secret_number:

        print("too high")

    elif num ==  secret_number:

        print("congratulations💖")
        print(f"you have won in {attempt} attempt")
        break

else:

    print("badluck 😔")


    
    
