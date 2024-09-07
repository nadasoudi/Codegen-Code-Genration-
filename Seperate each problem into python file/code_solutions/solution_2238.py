import random

def random_list(n):
    l = []
    for i in range(n):
        l.append(random.randint(0,n))
    return l

def main():
    n = int(input("Enter the number of elements in the list: "))
    l = random_list(n)
    print(l)

if __name__ == "__main__":
    main()