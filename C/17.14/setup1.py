# setup.py
from distutils.core import setup, Extension

setup(name='prchar1',
      ext_modules=[
        Extension('prchar1', 
                  ['pyprchar1.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['prchar']
                  )
      ]
)



