#add
def add(x,y):
    return x+y
#sub
def sub(x,y):
    return x-y
#multi
def multi(x,y):
    return x*y

#div
def division(x,y):
    return x//y

print("Selection Operation :")
print("1 Addtion")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

while True:
    choice = (input("Enter choices for 1/2/3/4 : "))
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter number1 : "))
            num2 = float(input("Enter number2 : "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == '1':
            print(num1 ," + ",num2," =",add(num1,num2))

        elif choice == '2':
            print(num1 ," - ",num2," =",sub(num1,num2))

        elif choice == '3':
            print(num1 ," * ",num2," =",multi(num1,num2))

        elif choice == '4':
            print(num1 ," / ",num2," =",division(num1,num2))

        next_calculation =  input("More calculations?? Y/N")
        if next_calculation == 'N' or 'n':
            break
    else:
        print("Invalid input")