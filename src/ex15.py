from sys import argv

script, filename = argv

# Opens file named 'filename' and creates an instance of
# the file object returned which is named 'txt'
txt = open(filename)

print "Here's your file %r:" % filename
# Call method read() on the txt instance
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()
