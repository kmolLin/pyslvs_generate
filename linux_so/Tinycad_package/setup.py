from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules=[
    Extension("demo",
              sources=["rga.pyx"],
              libraries=["m"] # Unix-like specific
    )
]

# setup(
#     name = 'cython_lab',
#     ext_modules = cythonize(ext_modules),
# )

setup(
    #name = 'cython_lab',
    ext_modules = cythonize('*.pyx'),
    include_dirs=[numpy.get_include()]
)

