# The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for
# items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different
# increment (even negative; sometimes this is called the ‘step’)

list(range(-10, -100, -30))

# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which
# returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list,
# thus saving space.

# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something
# from which they can obtain successive items until the supply is exhausted.

# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable
# (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break
# statement. This is exemplified by the following loop, which searches for prime numbers

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

"""
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
"""

# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires
# no action.

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# This is commonly used for creating minimal classes

class MyEmptyClass:
    pass

# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new
# code, allowing you to keep thinking at a more abstract level. The pass is silently ignored


def initlog(*args):
    pass   # Remember to implement this!


# A match statement takes an expression and compares its value to successive patterns given as one or more case
# blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages),
# but it can also extract components (sequence elements or object attributes) from the value into variables.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none
# of the branches is executed.

# You can combine several literals in a single pattern using | (“or”)

"""
case 401 | 403 | 404:
    return "Not allowed"
"""

# The first statement of the function body can optionally be a string literal; this string literal is the function’s
# documentation string, or docstring.

# Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a
# value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value
# is called None (it’s a built-in name). Writing the value None is normally suppressed by the interpreter if it would
# be the only value written.

fib(0)
print(fib(0))
"""
None
"""

# A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may
# be an expression), and methodname is the name of a method that is defined by the object’s type. Different types
# define different methods. Methods of different types may have the same name without causing ambiguity.

