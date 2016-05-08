# setup.py
from distutils.core import setup, Extension

setup(name='sample4',
      ext_modules=[
        Extension('sample4', 
                  ['pysample4.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['sample']
                  )
      ]
)



