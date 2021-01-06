the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# alternatively we could use this :-)
# elements = range(6)

# now we can print them too
for i in elements:
    print "Element was: %d" % i

# other methods on lists, and in mutable sequences in general, are:
# .extend(x), where x is any iterable object
# .count(x), which counts the instances of x in the list
# .insert(i, x), which inserts x in position i
# .index(x), returns smallest k that satisfies s[k] == x
# .reverse()
# .sort()
# s *= n, updates s with its contents repeated n times
# .remove(x)
# del s[i:j:k], removes these elements from the list
