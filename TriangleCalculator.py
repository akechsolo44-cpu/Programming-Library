x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
z = float(input("Enter side 3: "))

if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")