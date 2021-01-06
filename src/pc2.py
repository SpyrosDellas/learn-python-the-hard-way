with open("pc2.txt", "r") as pc2:
    input = pc2.read()

result = []
checked = []
for char in input:
    if char not in checked:
        if input.count(char) == 1:
            result.append(char)
        else:
            checked.append(char)

print "".join(result)
