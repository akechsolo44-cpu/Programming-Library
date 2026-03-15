vehicle = input("Enter vehicle type (motorcycle/car/bus): ").lower()
hours = int(input("Enter parking hours: "))

if vehicle == 'motorcycle':
    first = 1
    extra = 0.5
elif vehicle == 'car':
    first = 2
    extra = 1
elif vehicle == 'bus':
    first = 3
    extra = 2
else:
    print("Invalide vehicle type")
    exit()

if hours <= 1:
    fee = first
else:
    fee = first + (hours - 1) * extra

print("Parking Fee: $", fee)


 