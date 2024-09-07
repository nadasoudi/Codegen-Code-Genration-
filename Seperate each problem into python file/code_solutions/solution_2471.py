import math

def convert(C):
    F = C * 9/5 + 32
    return F

def main():
    C = int(input("Enter the temperature in Celcius: "))
    print("The temperature in Farenheit is: ", convert(C))

if __name__ == "__main__":
    main()