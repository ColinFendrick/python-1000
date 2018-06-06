#!/usr/bin/env python3
prefix = ['DEGUB', 'WARNING', 'ERROR', 'MESSAGE']


def show_chars(num, token):
    return '\t' + (token * (num + 4))


def show(index, message):
    if (index < 1):
        index = 1
    if (index > len(prefix)):
        index = len(prefix)
    message = prefix[index - 1] + ": " + message
    stars = show_chars(len(message), '*')
    print(stars)
    print('\t ' + message + ' *')
    print(stars)


def Append(zpre):
    prefix.append(zpre)


Append("TEST")
show(999, "The is a test")
show(5, 'This is a test')
show(4, "message")
show(-10, 'So...')
