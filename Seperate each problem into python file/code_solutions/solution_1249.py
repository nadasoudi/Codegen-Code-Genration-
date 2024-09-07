def wrap(string, max_width):
    paragraph = ""
    for i in range(len(string)):
        paragraph += string[i] * max_width
    return paragraph

# Enter your code here. Read input from STDIN. Print output to STDOUT
string, max_width = input(), int(input())
print(wrap(string, max_width))

'''
Sample Input

ABCDEFGHIJKLMNOPQRSTUVWXYZ
Sample