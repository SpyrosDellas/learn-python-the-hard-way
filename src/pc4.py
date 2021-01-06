# Tip: urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough.
#
# nothing=12345
# and the next nothing is 44827

from urllib import urlopen


# running below code intially we get "Yes. Divide by two and keep going."
# for page 16044, i.e. we continue from page 8022

# Final result is peak.html


start_value = "8022"
address = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
next_string = urlopen(address.format(start_value)).read()
current_val = start_value

for i in range(400):
    next_val = []
    for char in next_string:
        if char.isdigit():
            next_val.append(char)
    if next_val == []:
        print "Page no:", "".join(current_val), next_string
        break
    next_string = urlopen(address.format("".join(next_val))).read()
    current_val = next_val
