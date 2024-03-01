def countChars(string):
    chars={}
    for char in string:
        if char in chars:
            chars[char]+=1
        else:
            chars[char]=1
    return chars
string="ethernet"
chars= countChars(string)
for char,count in countChars("ethernet").items():
    print(f"{char}: {count}")