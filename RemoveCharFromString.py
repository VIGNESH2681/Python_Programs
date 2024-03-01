original_str = "Helo, Everyone"

new_str = ""
for char in original_str:
    if char != ',':
        new_str = new_str + char
    else:
        char == ','
        new_str= new_str.replace(',','')
print("original_str:",original_str)
print("New_str:",new_str)

