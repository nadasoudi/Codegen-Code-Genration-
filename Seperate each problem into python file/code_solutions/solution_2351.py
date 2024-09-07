"""

import random

def heart_pattern(n):
    """
    This function prints the heart pattern of the given number n.
    """
    for i in range(n):
        print("*", end="")
    print()

def main():
    """
    This function prints the heart pattern of the given number n.
    """
    n = int(input("Enter the number of rows: "))
    heart_pattern(n)

if __name__ == "__main__":
    main