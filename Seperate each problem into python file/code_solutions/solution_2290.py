1. Open the first file
2. Read the first line
3. Read the second line
4. Compare the lines
5. Close the file

"""

# 1. Open the first file
f1 = open("file1.txt", "r")

# 2. Read the first line
line = f1.readline()

# 3. Read the second line
line = f1.readline()

# 4. Compare the lines
if line!= "":
    print(line)

# 5. Close