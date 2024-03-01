number=int(input("Enter the number: "))
string = str(number)
reverse_string=string[::-1]
print("Reversed string is: ",reverse_string)
if string == reverse_string:
    print("This number is palindrome")
else:
    print("This number is not a palindrome")