def even_odd(n):
    even = 0
    odd = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

n = int(input("Enter the number of numbers: "))
even, odd = even_odd(n)
print("Even numbers: ", even)
print("Odd numbers: ", odd)

"""