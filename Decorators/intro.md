## Decorators 

```
def add(x,y=2):
    return x + y 
```

Some functions to get information about functions:

```
print(add) 
print(add.__name__) 
print(add.__defaults__)
print(add.__code__.co_varnames)
print(add.__defaults__)
```


### Scenario

Let's say we have the code for adding two number and we want to also compute the time taken. 

``` 
#Wrapper function
def timer(func):
    def f(*args, **kwrgs):
        before =time() 
        rv = func(*args, **kwrgs) 
        after = time()
        print('elapsed', after- before)
        return rv
    return f

def add(x,y=2):
    return x + y 
add = timer(add) #Equivalent to timer

@timer
def sub(x,y=2):
    return x - y
```