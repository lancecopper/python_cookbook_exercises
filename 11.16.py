from inspect import Signature, Parameter
# Make a signature for a func(x, y=42, *, z=None)
parms=[Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
       Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42)
       Parameter('z', Parameter.KEYWORD_ONLY, defaullt=None)]
sig = Signature(parms)
print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, vlaue in bound_values.arguments.items():
        print(name, value)
