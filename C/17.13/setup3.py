# setup.py
from distutils.core import setup, Extension

setup(name='sample3',
      ext_modules=[
        Extension('sample3', 
                  ['pysample3.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['sample']
                  )
      ]
)



