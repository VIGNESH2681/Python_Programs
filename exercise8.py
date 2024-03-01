import random
names=input("Enter the names seperated by comma: ")
names_list=names.split(",")
length=len(names_list)
final_list=random.randint(0,length-1)
print(final_list)
print(f"{names_list[final_list]} will pay the bill")

