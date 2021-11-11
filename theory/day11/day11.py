
# Modules;

# A module is a file containing Python definitions and statements. The file
# name is the module name with the suffix .py appended. Within a module, the
# module’s name (as a string) is available as the value of the global
# variable __name__.

"""
import fibo

fibo.__name__
'fibo'
"""

# If you intend to use a function often you can assign it to a local name

"""
fib = fibo.fib
fib(500)
"""

# A module can contain executable statements as well as function definitions.
# These statements are intended to initialize the module. They are executed
# only the first time the module name is encountered in an import statement.
# (They are also run if the file is executed as a script.)
#
# Each module has its own private symbol table, which is used as the global
# symbol table by all functions defined in the module. Thus, the author of
# a module can use global variables in the module without worrying about
# accidental clashes with a user’s global variables. On the other hand,
# if you know what you are doing you can touch a module’s global variables
# with the same notation used to refer to its functions, modname.itemname.
#
# Modules can import other modules. It is customary but not required to place
# all import statements at the beginning of a module (or script, for that
# matter). The imported module names are placed in the importing module’s
# global symbol table.
#
# There is a variant of the import statement that imports names from a module
# directly into the importing module’s symbol table.

"""
from fibo import fib, fib2

fib(500)
"""

"""
from fibo import *

fib(500)
"""

# This imports all names except those beginning with an underscore (_). In
# most cases Python programmers do not use this facility since it introduces
# an unknown set of names into the interpreter, possibly hiding some things
# you have already defined.
#
# Note that in general the practice of importing * from a module or package
# is frowned upon, since it often causes poorly readable code. However, it is
# okay to use it to save typing in interactive sessions.

"""
import fibo as fib

fib.fib(500)
"""

"""
from fibo import fib as fibonacci

fibonacci(500)
"""

# Note For efficiency reasons, each module is only imported once per
# interpreter session. Therefore, if you change your modules, you must
# restart the interpreter – or, if it’s just one module you want to test
# interactively, use importlib.reload(), e.g.

"""
import importlib
importlib.reload(modulename)
"""

# Executing modules as scripts;

# When you run a Python module with 'python fibo.py <arguments>'
# the code in the module will be executed, just as if you imported it, but
# with the __name__ set to "__main__". That means that by adding this code at
# the end of your module

"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
"""

# You can make the file usable as a script as well as an importable module,
# because the code that parses the command line only runs if the module is
# executed as the “main” file

"""
python fibo.py 50
"""

# This is often used either to provide a convenient user interface to a
# module, or for testing purposes (running the module as a script executes a
# test suite).

# The Module Search Path;

# When a module named spam is imported, the interpreter first searches for a
# built-in module with that name. If not found, it then searches for a file
# named spam.py in a list of directories given by the variable sys.path.
# sys.path is initialized from these locations:
#
# The directory containing the input script (or the current directory when no
# file is specified).
#
# PYTHONPATH (a list of directory names, with the same syntax as the shell
# variable PATH).
#
# The installation-dependent default (by convention including a site-packages
# directory, handled by the site module).


# “Compiled” Python files;

# To speed up loading modules, Python caches the compiled version of each
# module in the __pycache__ directory under the name module.version.pyc,
# where the version encodes the format of the compiled file; it generally
# contains the Python version number. For example, in CPython release 3.3
# the compiled version of spam.py would be
# cached as __pycache__/spam.cpython-33.pyc. This naming convention allows
# compiled modules from different releases and different versions of Python
# to coexist.

# Some tips for experts:
#
# You can use the -O or -OO switches on the Python command to reduce the size
# of a compiled module. The -O switch removes assert statements,
# the -OO switch removes both assert statements and __doc__ strings. Since
# some programs may rely on having these available, you should only use this
# option if you know what you’re doing. “Optimized” modules have an opt- tag
# and are usually smaller. Future releases may change the effects of
# optimization.
#
# A program doesn’t run any faster when it is read from a .pyc file than when
# it is read from a .py file; the only thing that’s faster about .pyc files
# is the speed with which they are loaded.
#
# The module compileall can create .pyc files for all modules in a directory.


# Standard Modules;

# The variable sys.path is a list of strings that determines the interpreter’s
# search path for modules. It is initialized to a default path taken from the
# environment variable PYTHONPATH, or from a built-in default if PYTHONPATH
# is not set. You can modify it using standard list operations

"""
import sys

sys.path.append('/ufs/guido/lib/python')
"""

# The dir() Function

# The built-in function dir() is used to find out which names a module
# defines. It returns a sorted list of strings

"""
import fibo, sys

dir(fibo)
['__name__', 'fib', 'fib2']

dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__',...]
"""

# Without arguments, dir() lists the names you have defined currently

"""
import fibo
fib = fibo.fib
dir()
['__builtins__', '__name__', 'fib', 'fibo', 'sys']
"""

# Note that it lists all types of names: variables, modules, functions, etc.

# Packages;

# Packages are a way of structuring Python’s module namespace by using
# “dotted module names”. A possible structure for your package (expressed
# in terms of a hierarchical filesystem)

"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""

# The __init__.py files are required to make Python treat directories
# containing the file as packages. This prevents directories with a common
# name, such as string, unintentionally hiding valid modules that occur later
# on the module search path. In the simplest case, __init__.py can just be
# an empty file,

# Users of the package can import individual modules from the package

"""
import sound.effects.echo
"""

# This loads the submodule sound.effects.echo. It must be referenced with
# its full name.

"""
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
"""

# An alternative way of importing the submodule

"""
from sound.effects import echo

echo.echofilter(input, output, delay=0.7, atten=4)
"""

# Yet another variation is to import the desired function or variable directly

"""
from sound.effects.echo import echofilter

echofilter(input, output, delay=0.7, atten=4)
"""

# Contrarily, when using syntax like import item.subitem.subsubitem, each
# item except for the last must be a package; the last item can be a module
# or a package but can’t be a class or function or variable defined in the
# previous item.

# Importing * From a Package;

# The only solution is for the package author to provide an explicit index of
# the package. The import statement uses the following convention: if a
# package’s __init__.py code defines a list named __all__, it is taken to be
# the list of module names that should be imported when
# 'from package import *' is encountered. It is up to the package author to
# keep this list up-to-date when a new version of the package is released.
# Package authors may also decide not to support it, if they don’t see a use
# for importing * from their package. For example, the file
# 'sound/effects/__init__.py' could contain the following code:

"""
__all__ = ["echo", "surround", "reverse"]
"""

# This would mean that from sound.effects import * would import the three
# named submodules of the sound package.
#
# If __all__ is not defined, the statement from sound.effects import * does
# not import all submodules from the package sound.effects into the current
# namespace; it only ensures that the package sound.effects has been imported
# (possibly running any initialization code in __init__.py) and then imports
# whatever names are defined in the package.

# Intra-package References;

# You can also write relative imports, with the from module import name form
# of import statement. These imports use leading dots to indicate the current
# and parent packages involved in the relative import. From the surround
# module for example, you might use

"""
from . import echo
from .. import formats
from ..filters import equalizer
"""

# Note that relative imports are based on the name of the current module.
# Since the name of the main module is always "__main__", modules intended
# for use as the main module of a Python application must always use absolute
# imports.

