# Accessing nested list elements
al = [1, 2, 'Spyros', 3]
ab = [al, al]
print "\n", ab
print ab[1][2]


# Modifying a list while looping on its elements
ac = ["alpha", "gamma", "european"]
print "\n", ac
for i in ac[:]:  # loops over a slice copy of the list
    if len(i) > 5:
        ac.insert(0, i)
print ac


# Playing with functions and function names
def fib(upper_limit, dummy1 = None, dummy2 = None):
    result = []
    a, b = 0, 1
    while a + b < upper_limit:
        result.append(b)
        a, b = b, a + b

    return result

print fib(500, dummy2 = "dummy")
fibonacci = fib  # Name fibonacci now is linked to fib
print fibonacci(upper_limit = 500)


# Using the raise statement
# raise ValueError("I don't like that!")
print "Let's continue...\n"


# Playing with dictionaries. Remember dictionaries are intrinsically unsorted
dict1 = {"name": "Spyros", "surname": "Dellas", "age": 37}
dict2 = dict(a = 1, b = 2, c = 3, d = 4)
dict3 = {x: x ** 2 for x in range(5)}
print dict1
print dict2
print dict3
print dict1['name']
print dict1.keys()
print sorted(dict1.keys()), "\n"


# Unpacking argument lists and dictionaries for a function call
# EXAMPLE 1 - UNPACKING AN ARGUMENT LIST
list1 = [2, 10, 2]
print range(*list1)

# EXAMPLE 2 - UNPACKING AN ARGUMENT DICTIONARY
def dummy_a(surname, name, age):
    print "My name is", name, surname, "and I'm", age, "years old.\n"

dummy_a(**dict1)
