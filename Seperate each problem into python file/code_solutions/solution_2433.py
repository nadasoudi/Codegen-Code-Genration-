def remove_odd_index(string, index):
    return string[:index] + string[index+1:]

def main():
    string = input("Enter String: ")
    index = int(input("Enter Index: "))
    print(remove_odd_index(string, index))

if __name__ == "__main__":
    main()

"""

def remove_odd_index(string, index):
    return string[:index] + string[index+1