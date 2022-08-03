#Example of yield when there is need to run function in an order or so. 

class Api:
    def run_this_first(self):
        first() 
    def run_this_second(self):
        second()
    def run_this_third(self):
        third()

def api():
    first()
    yield 
    second() 
    yield 
    third()
