year=int(input("Which year you want to check? "))

if year %4==0:
    if year%100==0:
        if year%400==0:
            print("It's a leap Year")
        else:
            print("Not a leap year ")
    else:
        print("It's a Leap Year ")
else:
    print("Not a Leap Year")