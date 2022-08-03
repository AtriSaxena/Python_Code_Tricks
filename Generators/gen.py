#gen.py 

# Top level syntax, function -> underscore method
# x()         __call__
from time import sleep

def add1(x,y):
    return x + y 

class Adder:
    def __call__(self, x, y): 
        return x + y 
add2 = Adder() 

# Function using the storage and eager waiting 
def compute():
    rv = [] 
    for i in range(10): 
        sleep(0.5)
        rv.append(i)
    return rv

# Same function 
# class Compute:
#     def __iter__(self):
#         self.last = 0
#         return self 
#     def __next__(self):
#         rv = self.last 
#         self.last +=1 
#         if self.last >10: 
#             raise StopIteration() 
#         sleep(0.5)
#         return rv 

# Function with no storage and result are returned instantly to consume 
# Generators 
def compute():
    for i in range(10):
        sleep(0.5)
        yield i # Yield not only return value but also return the control back


for val in compute():
    print(val) 