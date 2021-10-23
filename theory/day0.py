# print() is a function; also includes a newline;
print("This line will be printed.")

# Indentation;
# Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but
# the standard indentation requires standard Python code to use four spaces.

x = 1
if x == 1:
    print("x is 1.")

# Variables and Types;
# Python is completely object oriented, and not "statically typed". You do not need to declare variables
# before using them, or declare their type. Every variable in Python is an object.

# Numbers;
# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals).
# It also supports complex numbers, but we don't need them now.

# integers
my_integer_num = 7
print(my_integer_num)
my_integer_num = int(7.0)
print(my_integer_num)

# floats

my_float_number = 7.0
print(my_float_number)
my_float_number = float(7)
print(my_float_number)

# Strings;
# Strings are defined either with a single quote or a double quotes.

my_string = 'hello'
print(my_string)
my_string = "hello"
print(my_string)

# The difference between the two is that using double quotes makes it easy to include
# apostrophes (whereas these would terminate the string if using single quotes)

my_string = "hello, don't give up!"
print(my_string)

# Assignments;
# Simple operators can be executed on numbers and strings

three = 3
seven = 7
ten = three + seven
print(ten)

first_name = "Elon"
last_name = "Musk"
full_name = first_name + " " + last_name
print(full_name)

# Assignments can be done on more than one variable "simultaneously" on the same line

name, age = "Elon", 45
print(name, age)

# Mixing operators between numbers and strings is not supported

team1 = 2
team2 = 0
team_sum = " is two."

"""print(team1 + team2 + team_sum)"""

# Milestone exercise

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# Lists;
# Lists are very similar to arrays. They can contain any type of variable, and they can contain
# as many variables as you wish. Lists can also be iterated over in a very simple manner.

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3
print(mylist[-1])  # prints 3; think like ( -1 % 3 = 2 )
"""print(mylist[3])"""  # Accessing an index which does not exist generates an exception

for x in mylist:
    print(x)

# Arithmetic Operators
# The addition, subtraction, multiplication, and division operators can be used with numbers.

number = 11 + 21 * 31 / 14.0
print(number)

# The modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.

remainder = 112 % 3
print(remainder)

# Using two multiplication symbols makes a power relationship.

linear = 4 ** 1
squared = 16 ** 2
cubed = 10 ** 3
print(linear)
print(squared)
print(cubed)

# Using operators with Strings
# Python supports concatenating strings using the addition operator

full_name = "Elon" + " " + "Musk."
print(full_name)

# Python also supports multiplying strings to form a string with a repeating sequence

command = "Go " * 3
print("3 2 1 " + command)

# Using operators with Lists
# Lists can be joined with the addition operators (concatenate one list to another)

evens = [2, 4, 6, 8]
odds = [1, 3, 5, 7]
odds_and_evens = odds + evens
print(odds_and_evens)

# Python supports forming new lists with a repeating sequence using the multiplication operator

print([1, 2, 3, 4, 5] * 3)

# Milestone Exercise

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# String Formatting;
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format
# a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains
# normal text together with "argument specifiers", special symbols like "%s" and "%d".

name = "Elon"
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses)

name = "Elon"
age = 45
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using the %s operator as well. The string which returns
# from the "repr" method of that object is formatted as the string.

my_list = [1, 2, 3]
print("A list: %s" % my_list)
print("One: %s Two: %s Three: %s" % (my_list[0], my_list[1], my_list[2]))

# some basic argument specifiers
# %s                        - String (or any object with a string representation, like numbers)
# %d                        - Integers
# %f                        - Floating point numbers
# %.<number of digits>f     - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X                     - Integers in hex representation (lowercase/uppercase)

# Pay attention to this example! Each item reached by %s argument specifier

data = ("Elon", "Musk", 53.44)
format_string = "Hello %s %s. Your current balance is $%s billion."

print(format_string % data)

# Basic String Operations;
# len()

msg = "Hello world!"
print(len(msg))

# index()

print(msg.index("o"))

# count()

print(msg.count("l"))

# [inclusive:exclusive]

print(msg[3:7])

# If you just have one number in the brackets, it will give you the single character at that index.

print(msg[3])

# If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left

print(msg[:3])

# in. If you leave out the second number, it will give you a slice from the first number to the end.

print(msg[3:])

# You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string
# instead of the beginning. This way, -X means "Xth character from the end".

print(msg[-4])

# [start:stop:step]; This prints the characters of string from start to stop skipping step-amount of character.

print(msg[1:8:1])
print(msg[1:8:2])

# You can  reverse a string

print(msg[::-1])

# Make a new string with all letters converted to uppercase and lowercase, respectively.

print(msg.upper())
print(msg.lower())

# To determine whether the string starts with something or ends with something, respectively.

print(msg.startswith("Hello"))
print(msg.startswith("asd"))
print(msg.endswith("!"))
print(msg.endswith("asd"))

# To split the string into a bunch of strings grouped together in a list.

splitted_msg = msg.split(" ")
print(splitted_msg)
