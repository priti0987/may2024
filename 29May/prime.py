def prime(num):
    prime=[]
    for i in range(2,num+1):
        for j in range(2,num+1):
            if i%j == 0:
                break
        if i==j:
            prime.append(i)
    return prime


print(prime(10))