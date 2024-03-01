list1 = []
num = int(input("How many number you want to enter: "))
print("Enter the values: ")
for k in range(num):
    list1.append(int(input()))
print("unsorted List: ",list1)
for j in range(len(list1)-1):
    for i in range(len(list1) - 1-j):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            print(list1)
        else:
            print(list1)
    print()
print("Sorted List: ",list1)

