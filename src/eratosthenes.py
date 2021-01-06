from time import clock
import numpy as np


# Here we will try to optimize Eratosthenes sieve version 3 from previous
# exercise 'primes.py''.
# Version 3 needs 11.3 seconds for all primes up to 10^9. Our target is to
# do that in about 1 second....

def eratosthenes_v3(x):
    correction = x % 2
    length = (x + correction) / 2
    numbers = np.ones(length, dtype = np.bool_)
    numbers[0] = False
    last_num = x - 1 + correction

    sq_root = int(last_num ** 0.5)
    position = (sq_root + (sq_root % 2)) / 2 - 1

    for i in xrange(1, position):
        if numbers[i]:
            k1 = 2 * i
            k = k1 + i * i * 2
            step = k1 + 1
            numbers[k: :step] = False

    return  np.r_[2, 2 * numbers.nonzero()[0] + 1]


# This time we are going to use a wheel of (2,3) to improve memory
# usage and speed.
# Version 4 needs 8.75 seconds for all primes up to 10^9.
# Thus version 4 is 20% faster than version 3.
def eratosthenes_v4(x):
    x = int(x)
    if x < 2:
        return np.array([])
    elif x == 2:
        return np.array([2])
    elif x < 5:
        return np.array([2,3])

    # Next we create an array representing the following numbers:
    # [3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47,49,53,55...]
    length = ((x - 1 | 1) - 1) // 3 + 1
    numbers = np.ones(length, dtype = np.bool_)
    numbers[0] = 0

    last_num = (length * 3 - 2) | 1
    sq_root = int(last_num ** 0.5) - 1 | 1
    position = (sq_root - 1) // 3

    for i in xrange(1, position, 2):
        if numbers[i]:
            m = (3 * i + 4) * i + 1
            step = 6 * i + 4
            numbers[m: :step] = False
            numbers[(m + 2 * i + 1): :step] = False
        if numbers[i + 1]:
            m = (3 * i + 8) * i + 5
            step = 6 * i + 8
            numbers[m: :step] = False
            numbers[(m + 4 * i + 5): :step] = False

    return  np.r_[2, 3, (3 * numbers.nonzero()[0] + 1) | 1]

start = clock()
result = eratosthenes_v4(10 ** 7)
print result[-10:]
end = clock()
print "\n", end - start, "\n"

#start = clock()
#result =
#print result[-10:]
#end = clock()
#print "\n", end - start, "\n"
