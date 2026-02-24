price = float(input("Enter the item price: "))

if price >= 10000:
    discount = price * 0.05
    total = price - discount
else:
    total = price

print(f"Total payment: {total}") 