1. Open the first file
2. Open the second file
3. Read the contents of both files
4. Write the contents of the file to the second file
5. Close both files

"""

# 1. Open the first file
f1 = open("file1.txt", "r")

# 2. Open the second file
f2 = open("file2.txt", "r")

# 3. Read the contents of both files
print(f1.read())
print(f2.read())

#