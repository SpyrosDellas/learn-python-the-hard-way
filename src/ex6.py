# Asign a string to variable x. Formatter d means a decimal integer
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Formatter s means str() of the variables (already stings in this case)
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Formatter r means repr() of the variable and usually makes Python show quotes
# One exception is the repr(Boolean) which returns True/False without quotes
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
# This variable is a formatted string, but not yet evaluated/finalized!
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
