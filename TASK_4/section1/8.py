"""

**Weather Conditions**:
   - Above 30: Hot
   - 20 to 30: Warm
   - Below 20: Cold

"""

temperature = int(input ("enter the temperature: "))

if temperature > 30:
    print("-----HOT----")

elif temperature >=20 and temperature <=30:
    print("-----WARM----")

else:
    print("COLD")
