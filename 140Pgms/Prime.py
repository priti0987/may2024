#Prime

number = 230
flag = False
if number>1 :
    for i in range(2,number):
        if(number%i==0):
            flag = True
            break

if flag:
    print("given number is prime Not a number")
else:
    print("given number is prime number")