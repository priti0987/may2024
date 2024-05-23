# num = 4
# fac=1
# for i in range(1,num+1):
#     fac= fac*i
#
# print(fac)
# #6*5*4*3*2*1
# #4*3*2=24
#

factorial = 1
number = int(input("Enter a number :"))
if number<0:
    print("Factorial of neg numbers not possible")
elif number==0:
    print(f"factorial for {number} is 1")
else:
    for i in range(1,number+1):
        factorial = factorial*i
    print(f"factorial for given number is {factorial}")
