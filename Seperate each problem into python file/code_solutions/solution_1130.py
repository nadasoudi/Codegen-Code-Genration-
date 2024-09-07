import os

def alter_owner_and_group_id(file_name):
    # Open the file
    with open(file_name, 'r') as file:
        # Read the file
        data = file.read()
        # Change the owner
        data = data.replace('owner', 'owner_id')
        # Change the group id
        data = data.replace('group_id', 'group_id_id')
        # Write the file
        with