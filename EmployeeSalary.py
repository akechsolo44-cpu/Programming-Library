base_salary = 5000000
allowance = 750000

deduction = base_salary * 0.02
tax_deduction = base_salary * 0.05
total_deductions = deduction + tax_deduction

net_salary = base_salary + allowance - total_deductions

print(f"Net Salary: Rp {net_salary:,.2f}")