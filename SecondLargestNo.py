number = [9, 100, 101, 88, 3, 7]

largest = second = float('-inf')

for num in number:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("Second largest number is: ", second)