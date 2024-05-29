num = 123

revnumber = 0

while num>0:
    rem = num%10
    revnumber =revnumber*10+rem
    num//=10

print(revnumber)
