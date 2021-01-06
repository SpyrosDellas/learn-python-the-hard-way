from math import pi


s = "Hello\n"
print str(s)
# The repr() of a string adds string quotes and backslashes:
print repr(s)

print str(1.0/7)
print repr(1.0/7)

for x in range(1, 11):
    print repr(x).rjust(2), repr(x**2).rjust(3),
    print repr(x*x*x).rjust(4)

for x in range(1, 11):
    print "{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3)

print "We are the {} who say \"{}\"\n".format('knights', 'Ni')
print "{0} and {1}".format("spam", "eggs")
print "{1} and {0}".format("spam", "eggs")

print "\n{0} This {food} is {horrible}".format(
      "Whoao!", food="spam", horrible="tasty!")

print "\nThe value of Pi is approximately {}".format(pi)
print "\nThe value of Pi is approximately {!r}".format(pi)

# A demonstration of dynamic string formatting using braces within braces
digits = 50
print "\nThe value of PI rounded to {0} digits is {1:.{2}f}".format(
          digits, pi, digits)

print "\n The value of Pi is approximately %5.3f" % pi

table = dict(Spyros = 1234, Nick = 2131, Kostas = 3322)
for name, phone in table.items():
    print "{0:10} ==> {1:10d}".format(name, phone)

# Some file operations

with open("test.txt", "r") as f:
    for line in f:
        print line,
    f.seek(0)
    flist = f.readlines(0)
    print "\n%s" % flist
