#!/usr/bin/env python3
prefix = ('DEGUB', 'WARNING', 'ERROR', 'MESSAGE')


def show_chars(num, token):
    return '\t' + (token * (num + 4))

def show(index, message):
    index = index % 4
    message = prefix[index - 1] + ": " + message
    stars = show_chars(len(message), '*')
    print(stars)
    print('\t ' + message + ' *')
    print(stars)

show(4, 'This is a message')