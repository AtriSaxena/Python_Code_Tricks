from library import Base 

# First Case code 
# assert hasattr(Base, 'foo'), 'You break it you fool!'
# class Derive(Base):
#     def bar(self):
#         return self.foo()

# Second case code
class Derive(Base): 
    def bar(self): 
        return 'bar'