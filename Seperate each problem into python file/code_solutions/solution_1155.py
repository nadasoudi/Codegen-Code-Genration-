def index_of_char(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

# driver code
string = "Python is fun"
char = "P"

print(index_of_char(string, char))

# Output:
# -1
# -1
# -1
# -1
# -1
# -1
# -1
# -1