from random import randint

secret_number = randint(1,10)

for attempt in range(1,6):

    number = int(input("guess the number......."))

    if number == secret_number:

        print("congratulations 😍💖")
        break

else:

    print("badluck 🫠😔")  # for loopil break work chythaa ee else work akilla 