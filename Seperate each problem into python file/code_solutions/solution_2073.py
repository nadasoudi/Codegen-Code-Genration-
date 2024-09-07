import os

def reverseFile(fileName):
    with open(fileName, 'r') as f:
        data = f.readlines()
        data.reverse()
        with open(fileName, 'w') as f:
            f.writelines(data)

if __name__ == '__main__':
    fileName = 'input.txt'
    reverseFile(fileName)