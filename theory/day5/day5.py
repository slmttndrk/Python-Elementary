# Python is an interpreted language, which can save you considerable time during program development because no
# compilation and linking is necessary.

# Argument Passing;

"""
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings
and assigned to the argv variable in the sys module. You can access this list by executing import sys. The length of
the list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script
name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is
set to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module.
"""

# By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages
# in the world can be used simultaneously in string literals, identifiers and comments — although the standard
# library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display
# all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that
# supports all the characters in the file.

# To declare an encoding other than the default one, a special comment line should be added as the first line of
# the file. The syntax is as follows:

"""
# -*- coding: encoding -*-
"""

# where encoding is one of the valid codecs supported by Python.

# For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

"""
# -*- coding: cp1252 -*-
"""

# One exception to the first line rule is when the source code starts with a UNIX “shebang” line. In this case, the
# encoding declaration should be added as the second line of the file. For example:

"""
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""

# Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional
# result) you can use the // operator

print(17 // 3)

# In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using
# Python as a desk calculator, it is somewhat easier to continue calculations, for example:

"""
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
"""

# In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has
# built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by
# adding an r before the first quote:

"""
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
"""

# End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the
# end of the line.


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# produces the following output (note that the initial newline is not included):

"""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically
# concatenated. This feature is particularly useful when you want to break long strings:

"""
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
"""

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string
# results in an error.

# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

"""
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
"""

# Code that modifies a collection while iterating over that same collection can be tricky to get right.
# Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

