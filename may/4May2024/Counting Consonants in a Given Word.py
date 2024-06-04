vow = ['a','e','i','o','u']
myword = "pythonlovers"

count = 0

for i in myword:
    if i not in vow:
        count +=1
print(count)