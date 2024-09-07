import math

def display(number):
    print("{:^10}".format(number))

def left(number):
    display(number)
    print(" "*(10-len(str(number)))+str(number))

def right(number):
    display(number)
    print(" "*(10-len(str(number)))+str(number))

def center(number):
    display(number)
    print(" "*