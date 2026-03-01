price = float(input("Enter the item price: "))

if price >= 100000:
    discount = price * 0.10
    total = price - discount
else:
    total = price

print(f"Total payment: {total}") 