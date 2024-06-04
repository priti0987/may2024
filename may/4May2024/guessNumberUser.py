import  random

def comp_guess(x):
    print(x)
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H) , too low (L) or correct (C) ?? ").lower()
        if feedback == 'h':
            high =guess - 1
        elif feedback == 'l':
            low = guess+1
    print(f"yeee..! computor guess your number {guess} correctly..")


comp_guess(20)