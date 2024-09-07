import numpy as np

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter the number of terms: "))
print("Fibonacci series: ")
for i in range(n):
    print(fib(i))

# Solution:
#
# def fib(n):