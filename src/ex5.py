# Next line is added as a future reminder of how to tell Python to use
# the correct character encoding in case of errors
# -*- coding: utf-8 -*-

name = 'Spyros Dellas'
age = 37 # not a lie!
height = 1.78 # meters
height_inches = height * 39.3701 # in inches
weight = 74 # kgs
weight_pounds = weight * 2.20462 # in pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d meters tall." % height
 # Use format spec for a fixed point number with 2 decimal digits
print "He's {:.2f} meters tall.".format(height)
print "He's %d kgs heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight
)
print "This is a {}".format("test")
# Using r formatter we call repr() which usually shows representation in quotes
print "This is a {!r}".format("test")
