def get_colours(n):
    colours = ['red', 'green', 'blue']
    return colours[n % 3]

n = int(input("Enter the number of colours you want to choose: "))
print(get_colours(n))

"""

# Solution:

def get_colours(n):
    colours = ['red', 'green', 'blue']
    return colours[n % 3]

n = int