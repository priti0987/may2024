def sqr_num(n):
    return n*n

numberSS = [2,4,3,6,8]
print("Original",numberSS)
result = map(sqr_num,numberSS)
print("After using map function")
print(list(result))