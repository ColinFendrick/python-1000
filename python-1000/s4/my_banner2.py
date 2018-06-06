def show_chars(num, token):
    return "\t" + (token * (num + 4))


def show_banner(message):
    length = len(message)
    if length < 5:
        print(show_chars(len(message), "*"))
        print("\t* " + message + " *")
        print(show_chars(len(message), '*'))
    else:
        print(show_chars(len(message), "$"))
        print("\t* " + message + " *")
        print(show_chars(len(message), "$"))


show_banner('Doh!')
show_banner('brooooo this is python')
