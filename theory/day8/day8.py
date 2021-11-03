# Data Structures;

# More on Lists;

# append(x)
# Add an item to the end of the list.

# extend(iterable)
# Extend the list by appending all the items from the iterable.

# insert(i, x)
# Insert an item at a given position. The first argument is the index of the
# element before which to insert, so a.insert(0, x) inserts at the front of
# the list

# remove(x)
# Remove the first item from the list whose value is equal to x.

# pop([i])
# Remove the item at the given position in the list, and return it. If no
# index is specified, a.pop() removes and returns the last item in the list.

# clear()
# Remove all items from the list.

# index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal
# to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice
# notation and are used to limit the search to a particular subsequence of
# the list.

# count(x)
# Return the number of times x appears in the list.

# sort(*, key=None, reverse=False)
# Sort the items of the list in place

# reverse()
# Reverse the elements of the list in place.

# copy()
# Return a shallow copy of the list.

"""
x.__repr__() is useful when you want to see whether the returned value is
'None' or not.
"""

# Not all data can be sorted or compared. For instance, [None, 'hello', 10]
# doesn’t sort because integers can’t be compared to strings and None can’t
# be compared to other types. Also, there are some types that don’t have a
# defined ordering relation. For example, 3+4j < 5+7j isn’t a valid
# comparison.

# Using Lists as Stacks;
# The list methods make it very easy to use a list as a stack, where the
# last element added is the first element retrieved (“last-in, first-out”).
# To add an item to the top of the stack, use append(). To retrieve an item
# from the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.pop()

# Using Lists as Queues
# It is also possible to use a list as a queue, where the first element added
# is the first element retrieved (“first-in, first-out”); however, lists are
# not efficient for this purpose. While appends and pops from the end of list
# are fast, doing inserts or pops from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).
# To implement a queue, use collections.deque which was designed to have fast
# appends and pops from both ends.


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()

# List Comprehensions
# List comprehensions provide a concise way to create lists. Common
# applications are to make new lists where each element is the result of
# some operations applied to each member of another sequence or iterable,
# or to create a subsequence of those elements that satisfy a certain
# condition.

# For example, assume we want to create a list of squares, like:

squares = []
for s in range(10):
    squares.append(s**2)


# Note that this creates (or overwrites) a variable named s that still exists
# after the loop completes. We can calculate the list of squares without any
# side effects using:


squares = list(map(lambda x: x**2, range(10)))

# or, equivalently:

squares = [x**2 for x in range(10)]

# A list comprehension consists of brackets containing an expression followed
# by a for clause, then zero or more for or if clauses. The result will be a
# new list resulting from evaluating the expression in the context of the for
# and if clauses which follow it.

# this listcomp combines the elements of two lists if they are not equal


lc = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
"""
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""

# Note how the order of the for and if statements is the same in both these
# snippets.

# If the expression is a tuple (e.g. the (x, y) in the previous example),
# it must be parenthesized.

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[fruit.strip() for fruit in freshfruit]

[(x, x**2) for x in range(6)]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# List comprehensions can contain complex expressions and nested functions

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

# Nested List Comprehensions;
# The initial expression in a list comprehension can be any arbitrary
# expression, including another list comprehension.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns

[[row[i] for row in matrix] for i in range(4)]

# Unpacking Argument Lists;
# The reverse situation occurs when the arguments are already in a list or
# tuple but need to be unpacked for a function call requiring separate
# positional arguments. For instance, the built-in range() function expects
# separate start and stop arguments. If they are not available separately,
# write the function call with the *-operator to unpack the arguments out
# of a list or tuple:

list(range(3, 6))
"""
[3, 4, 5]
"""
args = [3, 6]
list(range(*args))
"""
[3, 4, 5]
"""

# In the same fashion, dictionaries can deliver keyword arguments with
# the **-operator:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# In the real world, you should prefer built-in functions to complex flow
# statements. The zip() function would do a great job for this use case:

list(zip(*matrix))  # another way of tranposing










