from urllib import urlopen
from HTMLParser import HTMLParser


class MyParser(HTMLParser):

    def handle_comment(self, data):
        MyParser.comment = data


address = "http://www.pythonchallenge.com/pc/def/equality.html"
page = urlopen(address).read()
parser = MyParser()
parser.feed(page)
problem_raw = parser.comment.strip()
problem = problem_raw.replace("\n", "")

result = []
for i in range(len(problem) - 6):
    first, second, third = False, False, False
    if problem[i:i+3].isupper():
        if i > 0:
            if problem[i-1].islower():
                first = True
    if problem[i+3].islower():
        second = True
    if problem[i+4:i+7].isupper():
        if i < len(problem) - 6:
            if problem[i+7].islower():
                third = True
    if first and second and third:
        result.append(problem[i+3])

print "".join(result)
