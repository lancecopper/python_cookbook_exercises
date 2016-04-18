import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0
    
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
            
@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)
        
print(add(2,3))
print(add(4,5))
print(add.ncalls)
s=Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print (Spam.bar.ncalls)
print(s.bar.ncalls)
Spam.bar(2,1)

class test:
    name='hero'
    pass

def blood(self, x):
    print('I got {0!r} blood, '.format(x), self.name)
c=types.MethodType(blood, test)
c(10)
