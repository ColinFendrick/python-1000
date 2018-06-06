#!usr/bin/env python3
def show_stars(num):
    return "\t*" + ("*" * (num + 3))


def show(message):
    stars = show_stars(len(message))
    print(stars)
    print("\t* " + message + " *">)

show('hey')
