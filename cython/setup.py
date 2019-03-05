from distutils.core import setup
from distutils.extension import Extension

import Cython
from Cython.Build import cythonize

extensions = [
   Extension("*", ["*.pyx"])
]

setup(
   name="Cython Extension",
   ext_modules=cythonize(extensions)
)
