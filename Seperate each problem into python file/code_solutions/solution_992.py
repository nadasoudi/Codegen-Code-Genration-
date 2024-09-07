def bigrams(words):
    # your code goes here
    return

"""

# Solution 1

def bigrams(words):
    return set(words)

# Solution 2

def bigrams(words):
    return {tuple(words[i:i+2]) for i in range(len(words))}

# Solution 3

def bigrams(words):
    return {tuple(words[i:i+2]) for i in range(