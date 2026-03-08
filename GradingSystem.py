score = int(input("Enter student score: "))

if score >= 85:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    garde = "C"
else:
    grade = "D"

print("Sore:", score)
print("Grade:", grade)