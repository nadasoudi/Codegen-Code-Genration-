def smallest_window(string):
    smallest_window = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string:
                smallest_window = string[i:j+1]
                break
    return smallest_window

print(smallest_window("abcdefghijklmnopqrstuvwxyz"))

"""

def smallest