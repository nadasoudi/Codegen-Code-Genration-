def array_to_string(arr):
    return ''.join(str(x) for x in arr)

def string_to_array(s):
    return [int(x) for x in s.split()]

def main():
    s = input("Enter a string: ")
    arr = string_to_array(s)
    print(array_to_string(arr))

if __name__ == "__main__":
    main