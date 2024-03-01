height=int(input("What is your height : "))
bill=0
if(height>=3):
    print("You can ride")
    age=int(input("Enter your age: "))
    if(age<12):
        bill=250
        print("You have to pay 250 Rs")
    elif(age<=18):
        bill=450
        print("You have to pay 450 Rs")
    else:
        bill=900
        print("You have to pay 900 Rs")
    want_photo=input("Do you want photo(Yes/No)")
    if want_photo=='yes' or want_photo=='Yes':
        bill=bill+50
        print(f"Your total bill is: {bill}  ")
else:
    print("can't Ride")
print("Thank You")