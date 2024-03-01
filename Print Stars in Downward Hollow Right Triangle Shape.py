n = int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == col or col == (n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()
