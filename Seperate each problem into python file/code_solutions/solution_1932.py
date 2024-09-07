import math

def cube(n):
    return math.pow(n,3)

def main():
    n = int(input("Enter the number of elements in the list: "))
    l = []
    for i in range(n):
        t = (int(input("Enter the element: ")),cube(i))
        l.append(t)
    print(l)

if __name__ == "__main__":