import re

str1 = "C O D E"
space = re.compile(r'\s+')
result = re.sub(space,'',str1)
# print(result)

resString = ""
for i in str1:
    if i != " ":
        resString = resString + i

print("result string ",resString)