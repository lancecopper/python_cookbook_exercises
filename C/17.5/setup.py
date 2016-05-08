# setup.py
from distutils.core import setup, Extension
setup(name='ptexample',
      ext_modules=[
        Extension('ptexample', 
                  ['ptexample.c'],
                  include_dirs = ['/home/lancecopper/code/C/17.5']    # May need pysample.h directory
                  )
        ]
)
