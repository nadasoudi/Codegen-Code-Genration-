import sys

def smallestSecondIndex(tup):
    # your code goes here
    return tup[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nt = input().split()

        n = int(nt[0])

        tup = []