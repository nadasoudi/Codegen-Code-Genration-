import string

def odd_index(string):
    odd_index = []
    for i in range(len(string)):
        if string[i] % 2!= 0:
            odd_index.append(string[i])
    return odd_index

print(odd_index("abcd"))

"""

def odd_index(string):
    odd_index = []
    for i in range(len(string)):
        if string[i]