Element1 = [11,54,66,33,88]
Element2 = [55,66,11,34,68]
Element3 = []

for i in Element1:
    if i in Element2:
        Element3.append(i)

print("First List:",Element1)
print("Second List:",Element2)
print("The common elements are: ",Element3)
