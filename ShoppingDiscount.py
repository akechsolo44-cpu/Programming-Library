total = int(input("Enter total amount: "))

if total  >= 500000:
    discount = total * 0.20
elif total >= 250000:
    discount = total * 0.10
else:
    discount = 0

final_price = total - discount

print("Discount:", discount)
print("Final amount to pay:", final_price)