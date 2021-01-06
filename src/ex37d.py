# A little function to return all primes up to x
# This function can return all primes up to 50000 in 11 seconds...
from time import clock

def primes_list_v1(x):
    p_list = [2]
    for num in range(3, x + 1, 2):  # Omit even numbers
        is_prime = True
        for num1 in range(2, int(num / 2) + 1):  # Test for primality up to num/2
            if num % num1 == 0:
                is_prime = False
                break
            else:
                continue
        if is_prime: p_list.append(num)
    return p_list

# start = clock()
# result = primes_list_v1(50000)
# end = clock()
# print end - start

# This optimized version is faster...
# Can return all primes up to 10^6 in 13 seconds...
def primes_list_v2(x):
    p_list = [2]
    for num in range(3, x + 1, 2):  # Omit even numbers
        is_prime = True
        for num1 in range(2, int(num ** 0.5) + 1): # Test up to sq. root of num
            if num % num1 == 0:
                is_prime = False
                break
            else:
                continue
        if is_prime: p_list.append(num)
    return p_list

# start = clock()
# result = primes_list_v2(1000000)
# end = clock()
# print result[-10:]
# print end - start

# This optimized version is even faster...
# Can return all primes up to 2*10^6 in 9.6 seconds...
from collections import deque

def primes_list_v3(x):
    p_list = deque([2, 3])
    for num in range(5, x + 1, 2):  # Omit even numbers
        is_prime = True
        if num % 3 == 0:
            is_prime = False
        else:
            # test numbers up to sqrt(num) starting from 5 with a step of 6
            # tests only num1 and num1 + 2
            # ommited numbers are even and multiples of 3
            # i.e. between 5 and 11, we ommit 6, 8, 9, 10
            for num1 in range(5, int(num ** 0.5) + 1, 6):
                if num % num1 == 0 or num % (num1 + 2) == 0:
                    is_prime = False
                    break
                else:
                    continue
        if is_prime: p_list.append(num)
    return p_list

# start = clock()
# result = primes_list_v3(2000000)
# end = clock()
# print "\n", end - start, "\n"


# All above algorithms use the trial division method, which is not very
# efficient. For larger numbers we need something better...
# In primes.py I've experimented with a faster set of algorithms,
# called prime number sieves.
