# setup.py
from distutils.core import setup, Extension

setup(name='prchar2',
      ext_modules=[
        Extension('prchar2', 
                  ['pyprchar2.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['prchar']
                  )
      ]
)



