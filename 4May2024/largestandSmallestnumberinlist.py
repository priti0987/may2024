myList = [5,55,65,85,123,5000,-1]

max=myList[0]
min = myList[0]


for i in myList:
    if i > max:
        max = i
    if i<min:
        min=i

print(min)
print(max)