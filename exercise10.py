heights=input("Enter all heights separated by a space: ")
height_list=heights.split()
count=0
for height in height_list:
    count=count+1
print(count)
for i in range (count):#0 1 2 3 4
    height_list[i]=int(height_list[i])
print((height_list))

total=0
for person in height_list:
    total+=person
avg=total/count
print(("Average of height is: ",round(avg)))