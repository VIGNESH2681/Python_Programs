sentence = input("Enter the Sentence: ")
string = sentence.lower()
count = 0
list1 = ['a',  'e', 'i', 'o', 'u']
for char in string:
    if char in list1:
        count = count+1
print("Total number of vowels in a given sentence: ", count)
