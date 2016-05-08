# setup.py
from distutils.core import setup, Extension

setup(name='prchar',
      ext_modules=[
        Extension('prchar', 
                  ['pyprchar.c'],
                  )
      ]
)



