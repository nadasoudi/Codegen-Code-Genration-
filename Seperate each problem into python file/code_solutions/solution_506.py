def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def read_file_as_array(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def write_file(filename, data):
    f = open(filename, 'w')
    for line in data: