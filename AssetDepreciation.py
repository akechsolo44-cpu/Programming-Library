initial_price = 12000000
salvage_value = 2000000
economic_life = 4

annual_depreciation = (initial_price - salvage_value) / economic_life
value_after_2_years = initial_price - (annual_depreciation * 2)

print(f"Annual Depreciation: Rp {annual_depreciation:,.2f}")
print(f"Value after 2 years: Rp {value_after_2_years:,.2f}")