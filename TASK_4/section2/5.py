

"""
5. Sleep Duration
- < 6: Sleep Deprived
- 6 – 8: Healthy Sleep
- > 8: Oversleeping


"""
sleep = float(input("Enter sleep duration (hours): "))

if sleep < 6:
    print("Sleep Deprived")
elif sleep <= 8:
    print("Healthy Sleep")
else:
    print("Oversleeping")