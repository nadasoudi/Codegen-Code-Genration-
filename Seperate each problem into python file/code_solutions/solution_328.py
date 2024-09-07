import random

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return content
    except IOError:
        print("Cannot open", filename)

def get_random_line(filename):
    lines = read_file(filename)
    return lines[random.randint(0, len(lines) - 1)]

print(get_random_line('/home/student