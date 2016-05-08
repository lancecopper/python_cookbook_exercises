# setup.py
from distutils.core import setup, Extension

setup(name='prchar3',
      ext_modules=[
        Extension('prchar3', 
                  ['pyprchar3.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['prchar']
                  )
      ]
)



