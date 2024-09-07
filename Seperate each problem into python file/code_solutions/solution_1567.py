import os

def get_size(path):
    size = os.path.getsize(path)
    print("Size of the file is: ", size)

def get_permissions(path):
    permissions = os.stat(path).st_mode
    print("Permissions of the file is: ", permissions)

def get_owner(path):
    owner = os.stat(path).st_uid