n = int(input("Enter the number of rows: "))

for row in range(n):
    for col in range(n):
        if col==0 or row == (n-1) or row == col:
            print("*",end="")
        else:
            print(end=" ")
    print()



