for i in range(4):
    for j in range(5):
        if j == 0 or j == 4:
            print("X", end=" ")
        elif j == 2:
            print("O", end=" ")
        elif (i == 1 or i == 2):
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()