import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper
    
#Example
@profiled
def add(x, y):
    return x + y

class Spam:
    @profiled
    def bar(self, x):
        print(self, x)
        

print(add(2,3))
print(add(4,5))
print(add.ncalls())
s=Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print (Spam.bar.ncalls())
print(s.bar.ncalls())
