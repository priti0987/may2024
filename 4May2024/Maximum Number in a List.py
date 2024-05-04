mylist = [12,56,89,41]
max = mylist[0]
print(max)
for i in mylist:
    if max < i:
        max = i

print("max is ",max)