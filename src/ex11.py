print "How old are you?",
age = raw_input()
"How tall are you?",
height = raw_input("How tall are you? ")
q1 = "How much do you weigh? "
weight = raw_input(q1)

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Note: input() function should be avoided due to security issues, because
# it will try to convert things entered as if they were Python code
