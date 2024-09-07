import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Argument passed:', sys.argv[1])
    else:
        print('No argument passed.')