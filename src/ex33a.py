def numbers(last_number, step):
    numbers = []

    for i in range(0, last_number, step):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num


numbers(10, 2)
