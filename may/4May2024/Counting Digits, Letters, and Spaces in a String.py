import re
str1 = "this string is having digits like 456789 and spaces"

digitCount = re.sub("[^0-9]","",str1)
letterCount = re.sub("[^a-zA-Z]","",str1)
spaceCount = re.findall("[ \n]",str1)


print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))

count1=0
for i in str1:
    if i.isdigit():
        count1 += 1
print("Number of digit in given string is :",count1)
countLetters = 0
for i in str1:
    if i.isalpha():
        countLetters +=1
print("Number of letters in given string is :",countLetters)

countspace = 0
for i in str1:
    if i.isspace():
        countspace +=1
print("Number of spaces in given string is :",countspace)
