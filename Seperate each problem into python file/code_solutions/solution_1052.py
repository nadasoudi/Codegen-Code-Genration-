import itertools

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(chunks(lst, 3)))
    print(list