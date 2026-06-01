def calculateovertimesalary(base_salary, total_hours_worked):
    if total_hours_worked > 40:
        overtime_hours = total_hours_worked - 40
        overtime_pay = overtime_hours * 50000
        return base_salary + overtime_pay
    else:
        return base_salary
    
print("Calculate Over Time Salary(50000, 45):", calculateovertimesalary(50000, 45))