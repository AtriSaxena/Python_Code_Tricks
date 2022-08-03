#dec.py 
# from inspect import getfile, getline
from time import time 

#Wrapper function
def timer(func):
    def f(x,y=10):
        before =time() 
        rv = func(x, y) 
        after = time()
        print('elapsed', after- before)
        return rv
    return f

# Higher order decorator
def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwrgs): 
            for _ in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwrgs)
            return rv 
        return wrapper 
    return inner 

@ntimes(2)
def add(x,y=2):
    return x + y 
add = timer(add) #Equivalent to timer

@timer
def sub(x,y=2):
    return x - y

print("add(10)", add(10))
print("add(10,20)", add(10,20))
print("add('x','y')", add('x','y'))

print("sub(10)", sub(10))
print("sub(10,20)", sub(10,20))
#print("add('x','y')", sub('x','y'))

# print(add) 
# print(add.__name__) 
# print(add.__defaults__)
# print(add.__code__.co_varnames)
# print(add.__defaults__)