a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest =  c 

print("Largest number:", largest)