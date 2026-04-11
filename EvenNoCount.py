numbers = [1, 5, 7, 8, 10, 18, 50]

even_count = 0

for num in numbers: 
    if num % 2 == 0:
        even_count += 1

print(even_count)