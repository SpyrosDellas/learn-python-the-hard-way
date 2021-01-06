# Using enumerate for looping

list1 = ["tic", "tac", "toe"]
for i in enumerate(list1):
    print i
for j, k in enumerate(list1):
    print j, k, "\n"


# Using zip and tuple unpacking for looping
questions = ["name", "quest", "favorite color"]
answers = ["Lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print "What is you {0}? It is {1}.".format(q, a)
    print "What is you %s? It is %s.\n" % (q, a)

# Looping through a dictionary using iteritems method
# Similar to enumerate, but the list of tuples created contains
# pairs of keys/values, instead of position/value

knights = {"Gallahand": "the pure", "Robin": "the brave"}
for j, k in knights.iteritems():
    print j, k
