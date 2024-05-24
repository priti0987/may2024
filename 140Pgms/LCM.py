def lcm(x,y):
    if x>y:
        grter = x
    else:
        grter = y
    while True:
        if (grter % x == 0) and (grter % y == 0):
            lcm=grter
            break
        grter+=1
    return lcm
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print("LCM",lcm(num1,num2))