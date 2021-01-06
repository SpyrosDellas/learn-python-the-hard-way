import sys

while True:

    try:
        x = float(raw_input("Please enter a number: "))

    # not_number is an instance of the exception class
    except ValueError as not_number:
        print type(not_number), not_number.args
        # We can also print not_number.args directly, as exceptions have
        # the __str__() method defined
        print not_number
        print "Oops! That wasn't a valid number. Try again..."

    except (EOFError, KeyboardInterrupt):
        print "Bye bye!"
        break

    except:
        print "Unexpected error...", sys.exc_info()[0]
        raise

    # If no exceptions occured in the code under try, execution
    # will branch here.
    else:
        print "Here's your number converted to an integer: {}".format(int(x))
        break

    # Exceptions or not the code under finally will execute anyway
    # as it's supposed to be clean-up code
    finally:
        print "Bye finally!"
