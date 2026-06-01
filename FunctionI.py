def calculatesplitbill(total_bill, num_of_people, tip_percentage):
    total_with_tip = total_bill + (total_bill * tip_percentage / 100)
    return total_with_tip / num_of_people

total_bill = float(input("Enter the total bill amount: "))
num_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

splitbill = calculatesplitbill(total_bill, num_of_people, tip_percentage)
print(f"Each person should pay: ${splitbill:.2f}")