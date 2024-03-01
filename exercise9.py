row1=[0,0,0]
row2=[0,0,0]
row3=[0,0,0]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the position where you want to hide money:")
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='x'
print(f"{row1}\n{row2}\n{row3}")