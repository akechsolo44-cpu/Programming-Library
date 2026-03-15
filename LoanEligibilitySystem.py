salary = float(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))
years = int(input("Enter employment years: "))

conditions = 0

if salary >= 3000:
    conditions +=1 
if credit_score >= 650:
    conditions +=1
if years >= 2:
    conditions +=1

if conditions == 3:
    print("Loan Approved")
elif conditions == 2:
    print("Conditional Approval")
else:
    print("Loan Rejected") 