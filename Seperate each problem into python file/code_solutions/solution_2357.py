def all_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substrings.append(string[i:j])
    return substrings

print(all_substrings("abcdefghijklmnopqrstuvwxyz"))

"""

def all_substrings(string):
    substrings = []
    for i in range(len(string)):