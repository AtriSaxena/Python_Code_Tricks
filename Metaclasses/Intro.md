## Case 

There are two groups working for a software. 

* Library group: Write core functionality as a library code. 
* Developer group: Write user code.  

Developer group takes code from library group and use that code to accomplish the tasks.


### Situation 
Suppose you are working on the Developer side and you can only use the library code. You cannot alter or modify the library.py source code. 


library.py
```
class Base:
    def foo(self):
        return "foo"
``` 

user.py 
```
from library import Base 

class Derive(Base):
    def bar(self):
        return self.foo()

```

```Where could this can break? ```  
Ans: If there is no foo function in Base class. 

```How can we check that there is foo function in Base class without calling the bar function or at import time itself? ``` 
Ans: We can call the assert ```hasattr()``` 


user.py 
```
from library import Base 

assert hasattr(Base, 'foo'), 'You break it you fool!'
class Derive(Base):
    def bar(self):
        return self.foo()

```


### Another Senario 

You are working on the library side of the code. You have no idea how user will use your code. 

You are assuming that User side developer will write the functionality of bar() function. 

library.py 
```
class Base: 
    def foo(self):
        return self.bar()
```

user.py 
```
class Derive(Base): 
    def bar(self): 
        return 'bar'

```

How will you force the user developer to write the bar function? 

Solution 1: Using the ```__build_class__``` 

```
class Base: 
    def foo(self):
        return self.bar()

old_bc = __build_class__ 
def my_bc(fun, name, base=None, **kw): 
    if base is Base:
        print("Check if bar method is defined.")
    if base is not None:
        return old_bc(fun, name, base, *kw)
    print("my buildclass ->", fun, kw)
    return old_bc(fun, name, **kw)

import builtins 
builtins.__build_class__ = my_bc
```

Solution 2: Using the Meta class