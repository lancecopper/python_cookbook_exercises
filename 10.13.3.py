#Base class. Uses adescriptro to set a value
class Descriptor:
    def __init__(self,name=None, **opts):
        self.name=name
        for key,value in opts.items():
            setattr(self, key, value)
            
    def __set__(self, instance, value):
        instance.__dict__[self.name]=value
        
        
#Descriptro for encforcing types
class Typed(Descriptor):
    expected_type=type(None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)
        
#Desciptor for encforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)
        
class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)
            
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance,value)
        
class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String, MaxSized):
    pass

# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            print('All:')
            print(key,value)
            if isinstance(value, Descriptor):
                print('selected:')
                print(key,value)
                value.name=key
        return type.__new__(cls, clsname, bases, methods)

# Example
class Stock2(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__=='__main__':
    s=Stock2('ACME', 74, 168.3)
    print(s.name)
