# Closures;
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
# A Nested Function is a function defined inside another function. It's very important to note that the nested
# functions can access the variables of the enclosing scope. However, at least in python, they are only readonly.
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.

def transmit_to_space(message):
    # "This is the enclosing function"
    def data_transmitter():
        # "The nested function"
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

# Without the nonlocal keyword, the output would be "3 9", however,
# with its usage, we get "3 3", that is the value of the "number" variable gets modified.


def print_msg(number):
    def printer():
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)


print_msg(9)

# Now, how about we return the function object rather than calling the nested function within.
# (Remember that even functions are objects. (It's Python.))


def transmit_to_space(message):
    def data_transmitter():
        print(message)
    return data_transmitter


dt = transmit_to_space("my message!")
dt()

# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved.
# This technique by which the data is attached to some code even after end of those other original functions
# is called as closures in python

# ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.
# (Eg. When there are few methods in a class, use closures instead). Also, Decorators in Python make extensive use
# of closures.

# Decorators;
# Decorators allow you to make simple modifications to callable objects like functions, methods, or classes.

"""
@decorator
def functions(arg):
    return "value"
"""


# Is equivalent to:

"""
def function(arg):
    return "value"
function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions
"""

# As you may have seen, a decorator is just another function which takes a functions and returns one.


def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)  # we run the old function
        old_function(*args, **kwds)  # we do it twice
    return new_function  # we have to return the new_function, or it wouldn't reassign it to the value


# This would make a function repeat twice.


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)
# 6
# 6

# You can also make it change the output


def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds)  # modify the return value
    return new_function


# You can also make it change the input


def one_input(old_function):
    def new_function(arg):  # only works if the old function has one argument
        return old_function(arg * 2)  # modify the argument passed
    return new_function


# You can also make it do checking.


def check(old_function):
    def new_function(arg):
        if arg < 0:
            raise (ValueError, "Negative Argument")  # This causes an error, better than it doing the wrong thing
        old_function(arg)
    return new_function


# If you want to multiply the output by a variable amount. You could define the decorator and use it


def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator


# Usage
@multiply(3)  # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num


# Now return_num is decorated and reassigned into itself
return_num(5)  # should return 15

# You can do anything you want with the old function, even completely ignore it!
# Advanced decorators can also manipulate the doc string and argument number.

# More understandable example;


def type_check(correct_type):
    def checker(old_function):
        def new_function(arg):
            if isinstance(arg, correct_type):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return checker


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

# Map, Filter, Reduce;
# Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer (you) to write simpler,
# shorter code, without neccessarily needing to bother about intricacies like loops and branching.
# Essentially, these three functions allow you to apply a function across a number of iterables, in one fell swoop.
# map and filter come built-in with Python (in the __builtins__ module) and require no importing. reduce, however,
# needs to be imported as it resides in the functools module. Let's get a better understanding of how they all work,
# starting with map.

# Map;
# The map() function in python has the following syntax:
# map(func, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on.
# Notice the asterisk(*) on iterables? It means there can be as many iterables as possible, in so far func has that
# exact number as required input arguments. Before we move on to an example, it's important that you note the following:

# 1. In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a
# generator object. To get the result as a list, the built-in list() function can be called on the map object.
# i.e. list(map(func, *iterables))

# 2. The number of arguments to func must be the number of iterables listed.

# Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase.
# Traditonally, in normal pythoning, I would do something like this:

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# With map() functions, it's not only easier, but it's also much more flexible.

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Which would also output the same result. Note that using the defined map() syntax above, func in this case is
# str.upper and iterables is the my_pets list -- just one iterable. Also note that we did not call the str.upper
# function (doing this: str.upper()), as the map function does that for us on each element in the my_pets list.

# What's more important to note is that the str.upper function requires only one argument by definition and so we
# passed just one iterable to it. So, if the function you're passing requires two, or three, or n arguments, then you
# need to pass in two, three or n iterables to it. Let me clarify this with another example.

# Say I have a list of circle areas that I calculated somewhere, all in five decimal places. And I need to round each
# element in the list up to its position decimal places, meaning that I have to round up the first element in the list
# to one decimal place, the second element in the list to two decimal places, the third element in the list to three
# decimal places, etc. With map() this is a piece of cake. Let's see how.

# Python already blesses us with the round() built-in function that takes two arguments -- the number to round up and
# the number of decimal places to round the number up to. So, since the function requires two arguments, we need to
# pass in two iterables.


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

#  "What if I pass in an iterable less than or more than the length of the first iterable? That is, what if I pass
#  range(1, 3) or range(1, 9999) as the second iterable in the above function". And the answer is simple: nothing!
#  Okay, that's not true. "Nothing" happens in the sense that the map() function will not raise any exception, it will
#  simply iterate over the elements until it can't find a second argument to the function, at which point it simply
#  stops and returns the result.

# So, for example, if you evaluate result = list(map(round, circle_areas, range(1, 3))), you won't get any error even
# as the length of circle_areas and the length of range(1, 3) differ. Instead, this is what Python does: It takes the
# first element of circle_areas and the first element of range(1,3) and passes it to round. round evaluates it then
# saves the result. Then it goes on to the second iteration, second element of circle_areas and second element of
# range(1,3), round saves it again. Now, in the third iteration (circle_areas has a third element), Python takes the
# third element of circle_areas and then tries to take the third element of range(1,3) but since range(1,3) does not
# have a third element, Python simply stops and returns the result, which in this case would simply be [3.6, 5.58].

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 3)))

print(result)

# To consolidate our knowledge of the map() function, we are going to use it to implement our own custom zip() function.
# The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the
# elements in the iterables. Like map(), in Python 3, it returns a generator object, which can be easily converted to a
# list by calling the built-in list function on it. Use the below interpreter session to get a grip of zip() before we
# create ours with map()

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

# Now our own custom zip() function

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# I didn't even need to create a function using the def my_function() standard way? That's how flexible map(), and
# Python in general, is! I simply used a lambda function. This is not to say that using the standard function
# definition method (of def function_name()) isn't allowed, it still is.
# I simply preferred to write less code (be "Pythonic").

# Filter;
# While map() passes each element in the iterable through a function and returns the result of all elements having
# passed through the function, filter(), first of all, requires the function to return boolean values (true or false)
# and then passes each element in the iterable through the function, "filtering" away those that are false.
# It has the following syntax:

# filter(func, iterable)

# The following points are to be noted regarding filter():

# 1. Unlike map(), only one iterable is required.
# 2. The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to
# it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# 3. filter passes each element in the iterable through func and returns only the ones that evaluate to true.
# I mean, it's right there in the name -- a "filter".

# The following is a list (iterable) of the scores of 10 students in a Chemistry exam. Let's filter out those who
# passed with scores more than 75...using filter.

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_a_student(score):
    return score > 75


over_75 = list(filter(is_a_student, scores))

print(over_75)

# The next example will be a palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same
# backwards as forwards. Let's filter out words that are palindromes from a tuple (iterable) of suspected palindromes.

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# Reduce
# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an
# initial argument. It has the following syntax:

# reduce(func, iterable[, initial])

# Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the
# optional value that gets placed before the elements of the iterable in the calculation, and serves as a default when
# the iterable is empty. The following should be noted about reduce(): 1. func requires two arguments, the first
# of which is the first element in iterable (if initial is not supplied) and the second element in iterable.
# If initial is supplied, then it becomes the first argument to func and the first element in iterable becomes
# the second element. 2. reduce "reduces" (I know, forgive me) iterable into a single value.

# Let's create our own version of Python's built-in sum() function. The sum() function returns the sum of all the items
# in the iterable passed to it.


from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)

# As usual, it's all about iterations: reduce takes the first and second elements in numbers and passes them to
# custom_sum respectively. custom_sum computes their sum and returns it to reduce. reduce then takes that result and
# applies it as the first element to custom_sum and takes the next element (third) in numbers as the second element
# to custom_sum. It does this continuously (cumulatively) until numbers is exhausted.

# Let's see what happens when I use the optional initial value.


from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers, 10)
print(result)

# The result, as you'll expect, is 78 because reduce, initially, uses 10 as the first argument to custom_sum.

# Nice exercise

from functools import reduce

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)

"""
[18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]
['olumide', 'josiah', 'omoseun']
24840
"""
