import sys

def replace_index(list, index, value):
    list[index] = value

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    replace_index(list, 2, 10)
    print(list)

if __name__ == "__main__":
    main()