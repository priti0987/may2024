list1 = [10,20,30]
list2 = [5,5,5]

reslist = []
for i in range(0 , len(list2)):
    reslist.append(list1[i]+list2[i])

print(reslist)