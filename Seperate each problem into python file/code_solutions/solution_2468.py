def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_heap(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_heap(n-1) + fib_heap(n-2)

def fib_heap_rec(n):