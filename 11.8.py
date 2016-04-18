from functools import wraps

class A:
    #Decorator as an instance method
    def decorator1(self, func):
        @wraps
