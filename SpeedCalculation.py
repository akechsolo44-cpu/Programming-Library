distance = float(input("Enter distance (km): "))
time = float(input("Enter time travelled (hours): "))

speed = distance / time

print("Average speed:", speed, ("km/hrs"))

if speed > 80:
    print("High speed")