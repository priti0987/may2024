myNumber = int(input("Enter a number"))

revNumbr = 0
while myNumber>0:
    # print(myNumber)
    revNumbr =   myNumber%10 + revNumbr*10
    myNumber = myNumber//10

# revNumbr = myNumber%10
# revNumbr = revNumbr*10
# myNumber = myNumber//10
print(revNumbr)
# print(myNumber)


str = input("Enter a string :")

print(str[::-1])



# print("reverse of given number",myNumber[:-1])
