def check_discount(total_price, ticket_quantity, coupon_code):
    if coupon_code == "NONTONSERU" and ticket_quantity >= 2:
        return total_price - 15000
    else:
        return total_price

print(check_discount(100000, 2, "NONTONSERU"))