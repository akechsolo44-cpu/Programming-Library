distance = 180
consumption_rate = 40
fuel_price = 13000

liters_needed = distance / consumption_rate
total_cost = liters_needed * fuel_price

print(f"Total fuel cost: Rp {total_cost:,.2f}")