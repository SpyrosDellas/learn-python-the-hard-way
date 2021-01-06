from time import clock

# First will try Euler's sieve
# It needs 45 seconds for the primes up to 2*10^6...

def euler_sieve(x):
    if x < 2: return []
    if x == 2: return [2]
    if x == 3 or x == 4: return [2, 3]
    if x == 5: return [2, 3, 5]

    p_list = [2, 3]
    for num in range(5, x + 1, 6):
        p_list.append(num)
        if (num + 2) <= x:
            p_list.append(num + 2)
        else:
            break

    if x < 25:
        return p_list
    else:
        pass

    # Now p_list is [2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41,
    # 43, 47, 49, 53, 55, 59, 61, ...]
    # Starting from 5 we need to erase all multiples
    index = 2

    while p_list[index] ** 2 < p_list[-1]:
        comp_list = []
        num1 = p_list[index]
        for i in range(index, len(p_list)):
            composite = num1 * p_list[i]
            if composite <= p_list[-1]:
                comp_list.append(composite)
            else:
                break
        p_list = sorted(set(p_list) - set(comp_list))
        index += 1

    return p_list

# start = clock()
# result = euler_sieve(2 * 10 ** 6)
# end = clock()
# print "\n", end - start, "\n"


# Next we will try Eratosthenes sieve...
# It needs 20 seconds for the primes up to 10^8.

def eratosthenes_v1(x):
    numbers = range(1, x + 1, 2)   # [1, 3, 5, 7, 9, 11, 13, 15...]
    numbers[0] = 0
    last_num = numbers[-1]
    length = len(numbers)
    limit = last_num ** 0.5

    for prime in numbers:
        if prime == 0:
            continue
        prime_sq = prime * prime
        if prime_sq > last_num:
            break
        for i in xrange((prime_sq - 1) / 2, length, prime):
            numbers[i] = 0

    return [2] + filter(None, numbers)


# Let's optimize it...
# Version 2 needs 6.9 seconds for the primes up to 10^8. The last 4 seconds
# are actually the return statement.

def eratosthenes_v2(x):
    # First create a list of Boolean values representing each odd number
    # up to x, i.e. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,...]
    correction = x % 2
    length = (x + correction) / 2
    numbers = [True] * length
    numbers[0] = False   # number 1 is not a prime

    last_num = x - correction

    # Loop through the   up to the position representing the number
    # which is the square root of x or (x-1) if x is even
    sq_root = int(last_num ** 0.5)
    position = (sq_root + (sq_root % 2)) / 2 - 1
    for i in xrange(1, position):
        if numbers[i]:
            # First find the position k in our list representing
            # the number squared
            k = (i * i + i) * 2
            step = i * 2 + 1
            # Starting from position k with a step of 2*i+1, asign False to
            # corresponding elements in numbers
            # If we used a for loop instead, execution time would be tripled!
            numbers[k: :step] = [False] * ((length - k -1) // step + 1)

    return [2] + [j * 2 + 1 for j in xrange(length - 1) if numbers[j]]


# Now we will try to optimize it even further. With a little web search
# we learn about an efficient numpy array, called ones.
# Version 3 needs less than 1 second for all primes up to 10^8 and
# 11 seconds for all primes up to 10^9

import numpy as np

def eratosthenes_v3(x):
    # First create a list of Boolean values representing each odd number
    # up to x, i.e. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,...]
    correction = x % 2
    length = (x + correction) / 2
    # Create a numpy array of Booleans, with all elements set to True
    numbers = np.ones(length, dtype = bool)
    numbers[0] = False   # number 1 is not a prime

    last_num = x - 1 + correction

    # Loop through the list up to the position representing the number
    # which is the square root of x or (x-1) if x is even
    sq_root = int(last_num ** 0.5)
    position = (sq_root + (sq_root % 2)) / 2 - 1
    for i in xrange(1, position):
        if numbers[i]:
            # First find the position k in our list representing
            # the number squared
            k1 = 2 * i
            k = k1 + i * i * 2
            step = k1 + 1
            # Starting from position k with a step of 2*i+1, asign False to
            # corresponding elements in numbers
            # Numpy allows to asign False to all elements of the slice
            # without in a simple statement
            numbers[k: :step] = False

    # So far the algorithm needs only 0.8 seconds, i.e. it's 3.5 times
    # faster than v2
    # Next we optimize the return function using Numpy's nonzero() which
    # returns an array of the indices of numbers with value True
    # (1 is interpreted as True). The array created is two-dimensional
    # so we refer to its first element, which the actual indices.
    # We then convert those indices to the numbers they represent.

    return  np.r_[2, 2 * numbers.nonzero()[0] + 1]


start = clock()
result = eratosthenes_v3(10 ** 9)
print result[-10:]
end = clock()
print "\n", end - start, "\n"
