print "I will now count my chickens:"
# Calculates Hens, calculation order follows PEMDAS standard
# PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Sutraction
print "Hens", 25. + 30. / 6
# The % symbol in a / b is the modulus j, ie a / b remaining j,
print "Roosters", 100 - 25. * 3. % 4.

print "Now I will count the eggs:"

# Again calculating using PEMDAS order.
# If not sure, always use Parentheses in complex calculations
# The result of 1 / 4 is zero, as Python drops the decimal part
# Use 1. / 4 for full precision
print 3. + 2 + 1 - 5 + 4. % 2. - 1. / 4. + 6.

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "what is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
