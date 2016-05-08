# setup.py
from distutils.core import setup, Extension

setup(name='prwchar1',
      ext_modules=[
        Extension('prwchar1', 
                  ['pyprwchar1.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO', '1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['prwchar']
                  )
      ]
)



