height=int(input("Enter you height in feet: "))

if(height>=3):
    print("You can ride")
    age=int(input("Enter your age: "))
    if(age<12):
        print("You have to pay 250 Rs")
    elif(age<=18):
        print("You have to pay 450 Rs")
    else:
        print("You have to pay 900 Rs")
else:
    print("can't Ride")
print("Bye")