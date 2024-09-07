def frequency(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def main():
    string = input("Enter the string: ")
    freq = frequency(string)
    print(freq)

if __name__ == "__main__":
    main()

"""

def frequency(string):
    freq = {}