def format_address(street, city, province, postal_code):
    return f"Street: {street}, City: {city}, {province} ({postal_code})"

print(format_address("Jl. Merdeka 10", "Jakarta", "DKI Jakarta", "10110"))