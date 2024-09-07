import os

def create_file(filename, letters):
    with open(filename, 'w') as file:
        for letter in letters:
            file.write(letter)

def main():
    filename = 'file.txt'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', '