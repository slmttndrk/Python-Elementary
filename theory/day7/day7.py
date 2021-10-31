# Functions can also be called using keyword arguments of the form kwarg=value.


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    pass


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword
# arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of
# the form *name which receives a tuple containing the positional arguments beyond the formal parameter list.
# (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

"""
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
"""

# The use case will determine which parameters to use in the function definition


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


# As guidance:
# Use positional-only if you want the name of the parameters to not be available to the user. This is useful when
# parameter names have no real meaning, if you want to enforce the order of the arguments when the function is
# called or if you need to take some positional parameters and arbitrary keywords.

# Use keyword-only when names have meaning and the function definition is more understandable by being explicit
# with names or you want to prevent users relying on the position of the argument being passed.

# For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

# The least frequently used option is to specify that a function can be called with an arbitrary number of arguments.

def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'


# Small anonymous functions can be created with the lambda keyword.
# Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single
# expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function
# definitions, lambda functions can reference variables from the containing scope


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
# 22

# Documentation Strings;


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
"""
Do nothing, but document it.

    No, really, it doesn't do anything.
"""

# For Python, PEP 8 has emerged as the style guide that most projects adhere to; it promotes a very readable and
# eye-pleasing coding style. Every Python developer should read it at some point; here are the most important points
# extracted for you:

# Use 4-space indentation, and no tabs.
# 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation
# (easier to read). Tabs introduce confusion, and are best left out.

# Wrap lines so that they don’t exceed 79 characters.
# This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

# Use blank lines to separate functions and classes, and larger blocks of code inside functions.

# When possible, put comments on a line of their own.

# Use docstrings.

# Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).

# Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and
# lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument
# (see A First Look at Classes for more on classes and methods).

# Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8,
# or even plain ASCII work best in any case.

# Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a
# different language will read or maintain the code.
