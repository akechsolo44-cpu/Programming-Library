usage = float(input("Enter Electricity Usage (kWh): "))

if usage < 100:
    price = usage * 0.10
elif usage < 300:
    price = usage * 0.15
else:
    price = usage * 0.20

print("Total Electricity Bill: $", price)