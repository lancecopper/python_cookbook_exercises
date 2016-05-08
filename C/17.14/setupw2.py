# setup.py
from distutils.core import setup, Extension

setup(name='prwchar2',
      ext_modules=[
        Extension('prwchar2', 
                  ['pyprwchar2.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['prwchar']
                  )
      ]
)



