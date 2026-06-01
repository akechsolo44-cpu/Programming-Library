x = float(input("Enter side x: "))
y = float(input("Enter side y: "))
z = float(input("Enter side z: "))

if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")