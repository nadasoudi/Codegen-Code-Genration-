import datetime

def add_timestamp(filename):
    # Open the file in read mode
    with open(filename, 'r') as f:
        # Read the file content
        content = f.read()
        # Convert the content to a list of strings
        content = content.split('\n')
        # Iterate over the list of strings
        for line in content:
            # If the line is not empty
            if line:
                # Split the line into a list of words
                words = line