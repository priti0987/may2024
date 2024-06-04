import random
#user is gonna guess random number from comp

def guess(x):
    rNumber = random.randint(1,x)
    guess = 0
    while guess != rNumber:
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess <rNumber:
            print("low==>")
        elif guess>rNumber:
            print("High== >")
    print(f"Congrats You guess the number {rNumber} correctly")


guess(556)
