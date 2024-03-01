def reverse(str_r):
    str_r = str_r[::-1]
    return str_r

str_r = input("Enter the Sentence: ")
print(reverse(str_r))

def reverse_words(str_r):
    n=len(str_r)
    if (n==1):
        return str_r
    str2=str_r.split(" ")
    size = len(str2)
    rev_all=""
    for i in range(size):
        rev=reverse(str2[i])
        rev_all = rev_all+rev+" "
    print(rev_all)

