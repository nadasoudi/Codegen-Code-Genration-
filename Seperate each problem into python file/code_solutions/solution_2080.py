1. Open the file in read mode
2. Read the file line by line
3. Iterate through the lines
4. For each line, replace the word 'python' with 'python3'
5. Print the modified file

"""

# 1. Open the file in read mode
file = open('file.txt', 'r')

# 2. Read the file line by line
for line in file:
    # 3. Iterate through the lines
    for word in line.split():
        # 4