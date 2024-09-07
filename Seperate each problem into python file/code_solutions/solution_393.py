def main():
    size = int(input("Enter the size of the square matrix: "))
    elements = []
    for i in range(size):
        elements.append(list(map(int, input().split())))
    print(sum(elements[0]))

if __name__ == "__main__":