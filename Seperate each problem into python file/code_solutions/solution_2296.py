import os

def change_name(filename):
    # Open the file for reading
    f = open(filename, 'r')
    # Read the file
    text = f.read()
    # Close the file
    f.close()
    # Change the name
    text = text.replace('\n','')
    # Open the file for writing
    f = open(filename, 'w')
    # Write the file
    f.write(text)
    # Close the file