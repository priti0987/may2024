numberTilFibonci = int(input("Enter number : = "))

fi = [0,1]

for i in range(numberTilFibonci):
    fi.append(fi[-1]+fi[-2])

print(fi)