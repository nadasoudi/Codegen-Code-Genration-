import os

def get_size(path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                size += os.path.getsize(fp)
    return size

print(get_size('C:\\Users\\srin\\Desktop\\Python\\Python_Projects\\'))

"""