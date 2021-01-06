try:
    raise Exception('spam', 'eggs')

except Exception as user_exception:
    print type(user_exception)     # the exception instance
    print user_exception.args      # the exception arguments returned as a tuple
    print user_exception           # __str__ allows args to be printed directly
    x, y = user_exception.args
    print 'x =', x
    print 'y =', y
