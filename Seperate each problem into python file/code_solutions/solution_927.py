import os

def copy_file(source, destination):
    with open(source, 'r') as source_file:
        with open(destination, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)

if __name__ == '__main__':
    source = 'C:\\Users\\srin\\Desktop\\Python\\Python_Project\\sample.txt'
    destination = 'C:\\Users\\