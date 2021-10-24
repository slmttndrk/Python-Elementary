# Conditions; Python uses boolean logic to evaluate conditions.
# The boolean values True and False are returned when an expression is compared or evaluated.

var = 21
print(var == 21)
print(var == 31)
print(var < 31)

# Boolean operators
# The "and" and "or" boolean operators allow building complex boolean expressions

name = "Elon"
age = 23
if name == "Elon" and age == 23:
    print("Your name is Elon, and you are also 23 years old.")

if name == "Elon" or name == "Rick":
    print("Your name is either Elon or Rick.")

# The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container

name = "Elon"
if name in ["Elon", "Rick"]:
    print("Your name is either Elon or Rick.")

# Code Blocks;
# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as
# it is consistent. Notice that code blocks do not need any termination.

statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass

# A statement is evaulated as true if one of the following is correct:
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.

# Some examples for objects which are considered as empty:
# 1. An empty string: ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

# The 'is' operator;
# The "is" operator does not match the values of the variables, but the instances themselves.

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# The "not" operator;
# Using "not" before a boolean expression inverts it.

# The "for" loop;

primes = [2, 3, 5, 7, 11]
for prime in primes:
    print(prime)

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# The difference between range and xrange is that the range function returns a new list with numbers of
# that specified range, whereas xrange returns an iterator, which is more efficient.
# (Python 3 uses the range function, which acts like xrange).

for x in range(7):
    print(x)

for x in range(3, 8):
    print(x)

for x in range(3, 10, 2):
    print(x)

# The "while" loop;

count = 0
while count < 7:
    print(count)
    count += 1

# The "break" and "continue" statements;
# "break" is used to exit a "for/while" loop,
# "continue" is used to skip the current block, and return to the "for/while" statement

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# The "else" clause for loops;
# When the loop condition of "for/while" statement fails then code part in "else" is executed.
# If a "break" statement is executed inside the for loop then the "else" part is skipped.
# Note that the "else" part is executed even if there is a continue statement.

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Functions;
# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.


def my_function():
    print("Hello From My Function!")

# Functions may also receive arguments (variables passed from the caller to the function).


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))

# Functions may return a value to the caller, using the keyword- 'return' .


def sum_two_numbers(a, b):
    return a + b

# Function Call;
# Write the function's name followed by (), placing any required arguments within the brackets.


my_function_with_args("Elon", "Happy birthday!")
