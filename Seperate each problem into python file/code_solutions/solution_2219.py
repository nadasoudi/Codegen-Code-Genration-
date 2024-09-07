def rightShift(s):
    return s[::-1]

def leftShift(s):
    return s[::-1]

def main():
    s = input("Enter the string: ")
    print(rightShift(s))
    print(leftShift(s))

if __name__ == "__main__":
    main()

"""

# Time complexity: O(n)
# Space Complexity: O(n)

def rightShift(s):