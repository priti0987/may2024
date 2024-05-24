def hcm(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and y % i == 0:
            hcm = i
    return hcm


num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

print("HCM", hcm(num1, num2))
