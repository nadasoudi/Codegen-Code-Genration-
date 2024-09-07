import sys

def main():
    # Read the file into a variable called data.
    data = open('data.gov.txt', 'r')
    # Read the file into a variable called name.
    name = data.readline()
    # Read the file into a variable called last_name.
    last_name = data.readline()
    # Read the file into a variable called email.
    email = data.readline()
    # Read the file into a variable called