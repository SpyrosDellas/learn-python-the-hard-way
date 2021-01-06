def break_words(stuff):
    """This function will break up words for us.

    .split(s) is a string method that returns a list of the words
    in the string using s as the delimiter string.
    """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words.

    sorted(iterable) is a built-in function that returns a sorted list
    from the items in iterable.
    """
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off.

    .pop(i) is a mutable sequence method that removes element i from
    the sequence. If no i is specified, it defaults to -1 (the last
    item in the sequence)
    """
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop()
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
