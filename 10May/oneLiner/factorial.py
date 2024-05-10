import functools
n=5
fac = 1 if n == 0 else functools.reduce(lambda x,y:x*y,range(1,n+1))
print(fac)