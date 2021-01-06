def numbers(last_number, step):
    i = 0
    numbers = []

    while i < last_number:
        print "At the top i is %d" % i
        numbers.append(i)
        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num


numbers(10, 2)
