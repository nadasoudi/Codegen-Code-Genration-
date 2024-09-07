import sys

def find_permutation(permutation, input_list):
    for i in range(len(permutation)):
        if permutation[i] in input_list:
            return permutation[i]
    return -1

def main():
    input_list = []
    input_list = sys.stdin.readline().strip().split()
    input_list = list(map(int, input_list))
    permutation = []