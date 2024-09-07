def main():
    n = int(input("Enter the number of numbers you want to print: "))
    print("The first", n, "lucky numbers are: ")
    for i in range(n):
        print(random.randint(1, 100))

if __name__ == "__main__":
    main()

"""

# Solution

def main():
    n = int(input("Enter the number of numbers you want to print: "))
    print("The