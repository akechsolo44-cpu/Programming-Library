import math

num_people = 5
liters_per_person = 2.5
days_in_week = 7
gallon_capacity = 19
price_per_gallon = 19000

weekly_liters = num_people * liters_per_person * days_in_week
gallons_to_buy = math.ceil(weekly_liters / gallon_capacity)
total_budget = gallons_to_buy * price_per_gallon

print(f"Weekly requirement: {weekly_liters} Liters")
print(f"Gallons to purchase: {gallons_to_buy}")
print(f"Total budget: Rp {total_budget:,.2f}")