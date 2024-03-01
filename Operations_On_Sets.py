# name1={"vicky","vignesh"}
# name2={"vasanth","vijay","akash"}
# print(name1.union(name2))
set1={"vicky","vignesh","vasanth"}
set2={"vasanth","vijay","akash"}
set3={"saravana","vasanth","vishnu"}
print(set1 | set2 | set3)
print(set1.union(set2,set3))
print((set1.difference(set2)))#gives set1 not in set2
print((set1-set2))
