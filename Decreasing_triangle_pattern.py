num = int(input("Enter number of row you want? "))
for i in range(num):
    for j in range(i,num):
        print("*",end = " ")
    print()