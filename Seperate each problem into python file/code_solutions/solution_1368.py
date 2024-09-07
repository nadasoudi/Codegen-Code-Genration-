def convert_uppercase(string):
    return string.upper()

def convert_lowercase(string):
    return string.lower()

def remove_duplicate_letters(string):
    return ''.join(sorted(set(string)))

def main():
    string = input("Enter the string: ")
    print(convert_uppercase(string))
    print(convert_