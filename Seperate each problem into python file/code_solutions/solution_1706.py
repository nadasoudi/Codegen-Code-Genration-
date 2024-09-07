import os

def get_file_id(file_name):
    # Open the file
    with open(file_name, 'r') as f:
        # Read the file
        data = f.read()
        # Return the file id
        return data.split()[0]

# Call the function
print(get_file_id('C:\\Users\\srin\\Desktop\\Python\\Python_Project\\file_id.txt'))

"""

"""

"""

"""