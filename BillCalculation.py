bill_amount = float(input("Enter total bill (Rp): "))
num_people = int(input("Enter number of people: "))
tax_rate = 0.10

total_tax = bill_amount * tax_rate
total_bill = bill_amount + total_tax
per_person = total_bill / num_people

print(f"Total after tax: Rp {total_bill:,.2f}")
print(f"Each person pays: Rp {per_person:,.2f}")

