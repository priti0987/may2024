def rec_fibo(n):
    if n <= 1:
        return n
    else:
        return rec_fibo(n - 1) + rec_fibo(n - 2)

numb = int(input("Enter terms :"))
if numb <= 0:
    print("Please enter positive number ")
else:
    print("Fibonacci Series : ")
    for i in range(numb):
        print(rec_fibo(i))
