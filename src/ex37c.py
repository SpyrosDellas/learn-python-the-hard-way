# List comprehensions
#
# In ex37b.py we saw how to use map to create a list containing
# the cubes of the input list element, using map(lambda x: x ** 3, range(y))
# We can use a more elegant way; a list comprehension:

print [x ** 3 for x in range(11)], "\n"

# Here's the definition of a list comprehension:
# A list comprehension consists of brackets followed by an expression
# followed by a for clause, then zero or more for or if clauses

# Example with one for and one if clause
print [x for x in range(1, 21) if (x % 3 == 0)], "\n"

# Example with complex exression and a nested function
print [x + y for x, y in zip(range(1, 11), range(100, 110))]

# Example with a nested list comprehension, doing the same thing
# as the built-in function zip()
list1 = [1, "a", "alpha"]
list2 = [2, "b", "beta"]
list3 = [3, "c", "gamma"]
list4 = [4, "d", "delta"]
test_list = [list1, list2, list3, list4]

zipped_list = (
[[element[i] for element in test_list] for i in range(len(test_list[1]))]
)
print zipped_list
print zip(list1, list2, list3, list4), "\n"


# Using the del statement
list6 = range(20)
del list6[5:10]
print list6, "\n"


# Playing with tuples
# Reminder: Strings and tuples are immutable sequences
tup1 = (12,)
tup2 = tup1, (13, 14)
print tup2, tup2[0], "\n"

# Unpacking a tuple
a, b = tup2
print a, b, "\n"
