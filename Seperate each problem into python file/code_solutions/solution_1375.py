def remove_duplicate_words(string):
    # your code goes here
    return string.replace(string[0], '').replace(string[-1], '').replace(string[0], '').replace(string[-1], '')

# driver code
string = "This is a string"
print(remove_duplicate_words(string))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)