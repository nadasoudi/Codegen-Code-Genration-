python solution.py

"""

# Python program to sort a dictionary
# using Lambda
def sortDict(d):
    # return sorted(d.items(), key=lambda item: item[1])
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

# Python program to print
# sorted dictionary
def printDict(d):
    for key, value in d:
        print("%s : %s" % (key, value))