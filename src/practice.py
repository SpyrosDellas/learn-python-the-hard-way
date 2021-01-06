import sys

try:
    "some code..."  # This code is protected by the try statement
    pass
except (ZeroDivisionError, NameError):
    "some code..."  # This code will execute if one of the 2 exceptions occurs
except IOError as e:    #IOError is a subclass of EnvironmentError
    print "I/O error({0}): {1}, in {2}".format(e.errno, e.strerror, e.filename)
    # Above IOError attributes are inherited from base class EnvironmentError
    "some code..."  # This code will execute if a IOError occurs
except:
     print "Unexpected error:", sys.exc_info()[0]
     # Above line will print the exception type
     raise    # This will reraise the last occured exception
else:
    "some code..."  # This will execute if no exception occurs
    pass
finally:
    "some code..."  # This code is always executed before leaving the try block


while True:
    try:
        x = int(raw_input('Please enter a number: '))
        break
    except ValueError:
        print "That's not a number. Try again."
