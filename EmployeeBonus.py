salary = float(input("Enter Employee's Salary: "))
years = float(input("Enter Number of Years: "))

if years >= 10:
    bonus = salary * 25
elif years >= 5:
     bonus = salary * 15
elif years >= 1:
    bonus = salary * 5
else:
    bonus = salary * 0

print("Employee's Bonus: $", bonus)