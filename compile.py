'''
Created on May 25, 2013

@author: rasmadeus
'''

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("model.CopyKiller", ["model/copyKiller.py"]),
    Extension("model.CopyKillerThread", ["model/copyKillerThread.py"]),
    Extension("view.resources", ["view/resources.py"]),
    Extension("view.View", ["view/view.py"]),
    ]

setup(
    name = 'CopyKiller',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)