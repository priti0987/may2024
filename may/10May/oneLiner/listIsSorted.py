myList = [1,2,5,6,]

is_sorted = all(myList[i]<=myList[i+1] for i in range (len(myList) - 1))


print(is_sorted)