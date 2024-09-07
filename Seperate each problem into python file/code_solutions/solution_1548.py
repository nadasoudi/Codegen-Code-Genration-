# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def square_keys(d):
    for i in d:
        print(i, math.pow(i, 2))

if __name__ == '__main__':
    d = {}
    for i in range(1, 16):
        d[i] = i**2
    square_keys(d)