# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"

# \ denotes that the following character is special
# For example \n tells Python to continue in a new line
# We use r before the string to escape above rule
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
months1 = r"Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
print "Here are the months: ", months1

# Triple quotes are used for multiple line continuous output
# End of lines are automatically included in the string, even if blank
# We can use \ at the end of the line to prevent this behaviour
# See the two versions below
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
print """\
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.\
"""
