def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)
        
    #Accessor methods for n
    def get_n():
        return n
        
    def set_n(value):
        nonlocal n
        n = value
    
    #Attach as a funciton attributes
    func.get_n = get_n
    func.set_n = set_n
    return func
    
import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
