prefix = {1: "ERROR", 2: "DEBUG", 3: "WARNING", 4: "MESSAGE"}


def show_chars(length, char):
    return "\t" + (char * (length + 4))


def message_box(index, message):
    if (index < 1):
        index = 1
    if (index > len(prefix)):
        index = len(prefix)
    message = prefix[index] + ": " + message
    stars = show_chars(len(message), "*")
    print(stars)
    print('\t* ' + message + ' *')
    print(stars)

message_box(3, 'hasdf')
