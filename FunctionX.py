def calculateloyaltypoints(total_transaction, member_status):
    if member_status == False:
        return 0
    else:
        return total_transaction // 20000

print(calculateloyaltypoints(100000, True))