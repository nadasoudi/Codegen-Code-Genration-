import os

def write_list_to_file(list, filename):
    with open(filename, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

def main():
    filename = 'list.txt'
    write_list_to_file(['Python', 'is', 'awesome'], filename)
    print('File {} created.'.format(filename))

if __name__ == '__main__':