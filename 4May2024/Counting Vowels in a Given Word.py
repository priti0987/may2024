vow = ['a','e','i','o','u']
myword = "python lovers"

count = 0

for i in myword:
    if i in vow:
        count +=1
print(count)