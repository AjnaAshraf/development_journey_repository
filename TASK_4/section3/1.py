"""**Body Temp (°C)**: < 36 (Low), 36 – 37.5 (Normal), > 37.5 (Fever)
"""


temperature = int(input("enter temperature: "))

if temperature < 36:
    print("Low")

elif temperature >= 36 and temperature < 37.5:
    print("Normal")

else:
    print(" fever")