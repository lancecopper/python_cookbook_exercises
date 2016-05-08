# setup.py
from distutils.core import setup, Extension

setup(name='consumef',
      ext_modules=[
        Extension('consumef', 
                  ['pyconsumef.c'],
                  )
      ]
)



