"""
A tank has 500 liters water. 35% is used. Find remaining water.
"""

litres=int(input("enter the total litres of water in the tank: "))
percentage=int(input("enter the percentage of water that is used: "))

remaining_water=litres-(litres*(percentage/100))
print("the remaining water in the tank is: ",remaining_water,"liters")

