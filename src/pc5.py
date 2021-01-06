# Tip: peak hell sounds familiar ?
# Instruction: pronounce it
#
# Reading the source we see a file called banner.p

from urllib import urlopen
import pickle

address = "http://www.pythonchallenge.com/pc/def/banner.p"
problem = pickle.load(urlopen(address))

result = []
for element in problem:
    element_string = "".join([tup[0] * tup[1] for tup in element])
    result.append(element_string)

print "\n".join(result)

# and the printout reads: channel
