hourly_rate = float(input("Enter the pay rate per hour: "))
hours = float(input("Enter hours of work: "))
minutes= float(input("Enter minutes of work: "))

total_hour_decimal = hours + (minutes / 60)
total_payment = total_hour_decimal * hourly_rate

print(f"Total Payment: Rp {total_payment:,.2f}")