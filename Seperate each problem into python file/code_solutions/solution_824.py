import random

def random_color():
    return "#%06x" % random.randint(0x00ff00, 0xffffff)

def random_alphabet():
    return chr(random.randint(97, 122))

def random_value():
    return random.randint(0, 70)

def random_multiple():