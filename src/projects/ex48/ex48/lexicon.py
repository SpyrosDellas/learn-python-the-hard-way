lexicon = {'direction': ['north', 'south', 'east', 'west', 'down', 'up',
                        'left', 'right', 'back'],
            'verb': ['go', 'stop', 'kill', 'eat'],
            'noun': ['door', 'bear', 'princess', 'cabinet'],
            'stop': ['the', 'in', 'of', 'from', 'at', 'it']
            }

#def convert_numbers(s):
#    try:
#        return int(s)
#    except ValueError:
#        return None

def scan(stuff):
    words = stuff.lower().split()
    result = []
    for word in words:
        for key in lexicon:
            if word in lexicon[key]:
                result.append((key, word))
                break
        else:
            if word.isdigit():
                result.append(('number', int(word)))
            else:
                result.append(('error', word))
    return result

# stuff = raw_input('> ')
# scan(stuff)
