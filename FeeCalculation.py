hour = int(input("Enter parking hours: "))

if hour <= 2:
    fee = 5000
else:
    fee = 5000 + (hour - 2) * 3000

print("Total parking fee:", fee)