
#  The del statement;

# There is a way to remove an item from a list given its index instead of
# its value: the del statement. This differs from the pop() method which
# returns a value. The del statement can also be used to remove slices from
# a list or clear the entire list (which we did earlier by assignment of an
# empty list to the slice).

# In python del is a keyword and remove(), pop() are in-built methods. The
# purpose of these three are same but the behavior is different remove()
# method delete values or object from the list using value and del and pop()
# deletes values or object from the list using an index.

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
del a[2:4]
del a[:]

# del can also be used to delete entire variables

del a

# Referencing the name a hereafter is an error (at least until another value
# is assigned to it).

# There is also another standard sequence data type: the tuple.
# A tuple consists of a number of values separated by commas

t = 12345, 54321, 'hello!'
t[0]
"""
12345
"""
t
"""
(12345, 54321, 'hello!')
"""

# Tuples may be nested:

u = t, (1, 2, 3, 4, 5)
u
"""
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
"""

# Tuples are immutable:

t[0] = 88888
"""
TypeError: 'tuple' object does not support item assignment
"""

# but they can contain mutable objects:

v = ([1, 2, 3], [3, 2, 1])
v
"""
([1, 2, 3], [3, 2, 1])
"""

# Tuples are immutable, and usually contain a heterogeneous sequence of
# elements that are accessed via unpacking (see later in this section) or
# indexing (or even by attribute in the case of namedtuples). Lists are
# mutable, and their elements are usually homogeneous and are accessed by
# iterating over the list.

# A special problem is the construction of tuples containing 0 or 1 items:
# the syntax has some extra quirks to accommodate these. Empty tuples are
# constructed by an empty pair of parentheses; a tuple with one item is
# constructed by following a value with a comma (it is not sufficient to
# enclose a single value in parentheses).

empty = ()

# <-- note trailing comma

singleton = 'hello',

len(empty)
"""
0
"""
len(singleton)
"""
1
"""
singleton
"""
('hello',)
"""

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!' are packed together in a tuple. The
# reverse operation is also possible

x, y, z = t

# This is called, appropriately enough, sequence unpacking and works for any
# sequence on the right-hand side. Sequence unpacking requires that there
# are as many variables on the left side of the equals sign as there are
# elements in the sequence.

# Sets;
# Python also includes a data type for sets. A set is an unordered collection
# with no duplicate elements. Basic uses include membership testing and
# eliminating duplicate entries. Set objects also support mathematical
# operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets. Note: to
# create an empty set you have to use set(), not {}; the latter creates an
# empty dictionary

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# show that duplicates have been removed

print(basket)
"""
{'orange', 'banana', 'pear', 'apple'}
"""

# fast membership testing

'orange' in basket
"""
True
"""

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')


# unique letters in a
a

"""
{'a', 'r', 'b', 'c', 'd'}
"""

# letters in a but not in b
a - b
"""
{'r', 'd', 'b'}
"""

# letters in a or b or both
a | b
"""
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
"""

# letters in both a and b
a & b
"""
{'a', 'c'}
"""

# letters in a or b but not both
a ^ b
"""
{'r', 'd', 'b', 'm', 'z', 'l'}
"""

# Similarly to list comprehensions, set comprehensions are also supported

a = {x for x in 'abracadabra' if x not in 'abc'}
a

"""
{'r', 'd'}
"""

