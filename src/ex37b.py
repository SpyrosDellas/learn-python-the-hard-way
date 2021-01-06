# Lambda expressions
# EXAMPLE 1 - A FUNCTION RETURNING A LAMBDA FUNCTION
def incrementor(step):
    return lambda x: x + step

print incrementor(0.1)(1000), "\n"
dum1 = incrementor(0.1);  # dum1 is now equv. to lambda x: x + 0.1
print dum1(1000), "\n"

# EXAMPLE 2 - PASSING A LAMBDA EXPRESSION AS A FUNCTION ARGUMENT
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Sort above list using .sort(key = ..... ), which extracts a comparison key
# from each element in the list. key must be an one argument function
print pairs
pairs.sort(key = lambda element: element[1])
print pairs


# Using lists as stacks, i.e. adding/removing elements from the end
stack1 = [1, 3, 5]
print "\n", stack1

stack1.append(7)
stack1.append(9)
print stack1

stack1.pop()
stack1.pop()
print stack1


# Using lists as queues
# Althougn we can use .insert and .pop for adding/removing elements at
# the beginning of the list this operation is not memory efficient.
# We should use collections.deque(), creating an efficient "deque" object
# which is a generalization of stacks and queues
from collections import deque

queue1 = deque(["Alpha", "Beta", "Gamma", "Delta"])
print "\n", queue1

queue1.appendleft("Zero")
queue1.append("Epsilon")
print queue1

queue1.popleft()
queue1.pop()
print queue1


# Using filter(function, sequence)
def func1(x):
    return x % 5 == 0 or x % 7 == 0

list1 = range(101)
tup1 = tuple(list1)
print "\n", filter(func1, list1)
print "\n", filter(func1, tup1)
# We can also do it in one line of code, using a lambda function
print "\n", filter(lambda x: (x % 5 == 0 or x % 7 == 0), tup1)


# Using map(function, sequence [,sequence]*n)
# EXAMPLE 1 - USING MAP WITH ONE SEQUENCE
def cube(x):
    return x ** 3

print "\n", map(cube, range(11))
# We can also do it in one line of code, using a lambda function
print "\n", map(lambda x: x ** 3, range(11))

# EXAMPLE 2 - USING MAP WITH TWO SEQUENCES
def func2(a, b):
    return a + 2 * b

print "\n", map(func2, range(11), range(11, 22))
# We can also do it in one line of code, using a lambda function
print "\n", map(lambda a, b: (a + 2 * b), range(11), range(11, 22))


# Using reduce(function, sequence)
def factorial(x):
    return reduce(lambda a, b: a * b, range(1, x + 1))

print "\n", factorial(5)
