# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      ext_modules=[
        Extension('sample', 
                  ['17.6.2.c']
                  )
      ]
)



