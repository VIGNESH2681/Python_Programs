def LongestWordLength(string):
    l=0
    w=''
    words=string.split()
    for word in words:
        if (len(word) > l):
            w= word
            l= len(word)
    return(w,l)
string=input("Enter the String: ")
w,l = LongestWordLength(string)

print("Longest word is: ", w)
print("Length of the Longest word: ", l)

