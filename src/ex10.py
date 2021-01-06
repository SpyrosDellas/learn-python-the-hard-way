# \t is the horizontal TAB
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# \\ escapes \
# We can also use r"....." to escape all \ in a string
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

test1 = "\"Nice\" job. \a"
test2 = '\123 \xac \v \f'
test3, test4 = 10, True
test5 = 'Are there %d \'cats\' in this room? \n%s' % (test3, test4)
test6 = "\"It's a wonder!\" he said."
test7 = '\'It\'s a wonder!\' he said.'
test8 = u'Hello\u0020World!'  #u0020 is the space special character
test9 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test10, test11, test12 = test9[0], test9[:6], test9[6:]

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print test1
print test2
print test5
print "Here's test6 raw print-out: %r" % test6
print "Here's test7 raw print-out: %r" % test7
print "Here's test6 string print-out: %s" % test6
print "Here's test7 string print-out: %s" % test7
print test8
print "\n %s, %s, %s\n" % (test10, test11, test12)

# Next line initiates an endless loop with a nested loop
# while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#        print "%s\r" % i,
# Above line prints i and then returns the cursor back (same as using left arrow)
# The comma at the end tells Python to keep printing on same line
