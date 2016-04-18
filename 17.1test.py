import os
a=os.path.split(__file__)
print(a[-1])
_file = 'libsample.so'
print(os.path.split(__file__)[:-1])
b=(os.path.split(__file__)[:-1] + (_file,))
print(b)
print('###',os.path.split(__file__),'###')
