import os

# Create a symbolic link
os.symlink("/home/user/file.txt", "/home/user/file2.txt")

# Read the link
print(os.readlink("/home/user/file.txt"))

# Create a symbolic link
os.symlink("/home/user/file2.txt", "/home/user/file3.txt")

# Read the link
print(os.readlink