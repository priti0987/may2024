num = int(input("Enter a number "))
nums=str(num)
numbd = len(nums)

sumofp = 0
temp = num
while temp>0:
    digit = temp%10
    sumofp += digit**numbd
    temp//=10

if sumofp == num:
    print("Armstr")
else:
    print("not armstrong number")
