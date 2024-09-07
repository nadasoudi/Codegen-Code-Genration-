def main():
    numbers = input("Enter numbers separated by comma: ")
    numbers = numbers.split(",")
    numbers = tuple(numbers)
    print(numbers)

if __name__ == "__main__":
    main()

# OUTPUT:
# Enter numbers separated by comma: 1,2,3,4,5,6,7,8,9,10
# (1, 2