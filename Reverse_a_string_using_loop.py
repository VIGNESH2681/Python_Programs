def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string= i+reversed_string
    print("Reversed String: ",reversed_string)
string=input("Enter the String: ")
print("Enter String is: ",string)
reverse(string)