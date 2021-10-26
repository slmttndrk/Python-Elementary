# Numpy Arrays;
# Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that
# they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.

import numpy as np


height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Element-wise calculations;
# We can perform element-wise calculations on height and weight. For example, you could take all 6 of the height
# and weight observations above, and calculate the BMI for each observation with a single equation.
# These operations are very fast and computationally efficient.
# They are particularly helpful when you have 1000s of observations in your data.


bmi = np_weight / np_height ** 2
print(bmi)

# Subsetting;
# Another great feature of Numpy arrays is the ability to subset. For instance, if you wanted to know
# which observations in our BMI array are above 23, we could quickly subset it to find out.

print(bmi[bmi > 23])

# Pandas Basics;
# Pandas DataFrames;
# Pandas is a high-level data manipulation tool. It is built on the Numpy package and its key data structure
# is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and
# columns of variables. There are several ways to create a DataFrame. One way is to use a dictionary.


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}


import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

"""
     area    capital       country  population
0   8.516   Brasilia        Brazil      200.40
1  17.100     Moscow        Russia      143.50
2   3.286  New Dehli         India     1252.00
3   9.597    Beijing         China     1357.00
4   1.221   Pretoria  South Africa       52.98
"""

# As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the numerical
# values 0 through 4. If you would like to have different index values, say, the two letter country code,
# you can do that easily as well.

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas.
# The csv cars.csv is stored and can be imported using pd.read_csv

cars = pd.read_csv('cars.csv')
print(cars)

# Indexing DataFrames;
# There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square
# bracket notation. You can use square brackets to select one column of the cars DataFrame. You can either use
# a single bracket or a double bracket. The single bracket will output a Pandas Series, while a double bracket
# will output a Pandas DataFrame.

# Print out country column as Pandas Series
print(cars['cars_per_cap'])
# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])
# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Square brackets can also be used to access observations (rows) from a DataFrame.

# Print out first 4 observations
print(cars[0:4])
# Print out fifth and sixth observation
print(cars[4:6])

# You can also use loc and iloc to perform just about any data selection operation. loc is label-based, which means
# that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so
# you have to specify rows and columns by their integer index.

# Print out observation for Japan
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Generators;
# Generators are very easy to implement, but a bit difficult to understand. Generators are used to create iterators,
# but with a different approach. Generators are simple functions which return an iterable set of items, one at a time,
# in a special way. When an iteration over a set of item starts using the for statement, the generator is run.
# Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the
# for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite)
# as it wants, yielding each one in its turn.

import random


def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)

# This function decides how to generate the random numbers on its own, and executes the yield statements one at a time,
# pausing in between to yield execution back to the main for loop.


"""
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
"""

# List Comprehensions;
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []

for word in words:
    if word != "the":
        word_lengths.append(len(word))


print(words)
print(word_lengths)

# Using a list comprehension, we could simplify this process to this notation

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Multiple Function Arguments;
# Every function in Python receives a predefined number of arguments, if declared normally.


def myfunction(first, second, third):
    pass


# It is possible to declare functions which receive a variable number of arguments


def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))


# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter,
# using the following syntax.

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % result)

# Regular Expressions;
# Regular Expressions (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text.
# In Python, we have the re module. The applications for regular expressions are wide-spread, but they are fairly
# complex, so when contemplating using a regex for a certain task, think about alternatives, and come to regexes
# as a last resort.

# An example regex is r"^(From|To|Cc).*?python-list@python.org"

# Now for an explanation: the caret ^ matches text at the beginning of a line.
# The following group, the part with (From|To|Cc) means that the line has to start with one of the words that are
# separated by the pipe |. That is called the OR operator, and the regex will match if the line starts with any
# of the words in the group.
# The .*? means to un-greedily match any number of characters, except the newline \n character.
# The un-greedy part means to match as few repetitions as possible.
# The . character means any non-newline character, the * means to repeat 0 or more times, and the ? character makes
# it un-greedy.

# So, the following lines would be matched by that regex: From: python-list@python.org To: !asp]<,. python-list@python.org


# Exception Handling;
# When programming, errors happen. It's just a fact of life. Perhaps the user gave bad input. Maybe a network
# resource was unavailable. Maybe the program ran out of memory. Or the programmer may have even made a mistake!
# Python's solution to errors are exceptions.

# But sometimes you don't want exceptions to completely stop the program. You might want to do something special
# when an exception is raised. This is done in a try/except block.

def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            do_stuff_with_number(0)


catch_this()


# Sets;
# Sets are lists with no duplicate entries.

print(set("my name is Eric and Eric is my name".split()))

# Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between
# other sets.

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

# To find out which members attended only one of the events, use the "symmetric_difference" method.

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To find out which members attended only one event and not the other, use the "difference" method

print(a.difference(b))
print(b.difference(a))

# To receive a list of all participants, use the "union" method

print(a.union(b))

# Serialization;
# Python provides built-in JSON libraries to encode and decode JSON.

# There are two basic formats for JSON data. Either in a string or the object datastructure. The object datastructure,
# in Python, consists of lists and dictionaries nested inside each other. The object datastructure allows one to use
# python methods (for lists and dictionaries) to add, list, search and remove elements from the datastructure.
# The String format is mainly used to pass the data into another program or load into a datastructure.
# To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into
# the json object datastructure

import json
print(json.loads(json_string))

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String

import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# Python supports a Python proprietary data serialization method called pickle
# (and a faster alternative called cPickle).

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# Partial functions;
# You can create partial functions in python by using the partial function from the functools library.
# Partial functions allow one to derive a function with x parameters to a function with fewer parameters and
# fixed values set for the more limited function.

from functools import partial


def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x


p = partial(func, 5, 6, 7)
print(p(8))

"""
60
"""

# Code Introspection;
# Code introspection is the ability to examine classes, functions and keywords to know what they are, what they do
# and what they know. Python provides several functions and utilities for code introspection.

help()          # finds what other functions do
dir()           # return list of methods and attributes associated with that object
hasattr()       # Checks if an object has an attribute
id()            # returns a special id of an object
type()          # returns the type of an object
repr()          # Return string representation of object
callable()      # Checks if an object is a callable object (a function)or not
issubclass()    # Checks if a specific class is a derived class of another class
isinstance()    # Checks if an objects is an instance of a specific class
__doc__         # Return some documentation about an object
__name__        # Return the name of the object
