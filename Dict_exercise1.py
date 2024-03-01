students_mark={
    'vicky':91,
    'vasanth':78,
    'praba':87,
    'vishnu':56,
    'daya':67

}
students_grade={}
for student in students_mark:
    marks=students_mark[student]
    if marks>90:
        students_grade[student]="A+"
    elif marks>80:
        students_grade[student]="A"
    elif marks>70:
        students_grade[student]="B+"
    elif marks>60:
        students_grade[student] = "B"
    else:
        students_grade[student] = "C"

print(students_grade)

