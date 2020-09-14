import glob
from os.path import dirname, join, basename, isfile

currentPath = dirname(__file__)
modules = glob.glob(join(currentPath, "*.py"))
modules.remove(join(currentPath, "__init__.py"))
modules.remove(join(currentPath, "argsIF.py"))
__all__ = []
for module in modules:
    if isfile(module):
        __all__.append(basename(module[:-3])) # chop the .py off

# importing every file causes the auto registration to happen
from . import *
