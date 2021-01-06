from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# It is good practise to use the with keyword when dealing with file objects.
# The file is properly closed after its suite finishes, even if an exception
# is raised on the way.
with open(from_file) as in_file:
    indata = in_file.read()
# indata = open(from_file).read()

print "The input file is %d bytes long" %len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

with open(to_file, 'w') as out_file:
    out_file.write(indata)

print "Alright, all done."

# All above commands in two lines :-)
# with open(argv[1]) as in_file, open(argv[2], 'w') as out_file:
#     out_file.write(in_file.read())
