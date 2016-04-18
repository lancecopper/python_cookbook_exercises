from functools import wraps
import inspect

def func():
    pass

@wraps(func)
def wrapper(func, *args, debug=False, **kwargs):
    if debug:
        print('Calling', '')
    return func(*args, **kwargs)
    

print(inspect.signature(wrapper))
