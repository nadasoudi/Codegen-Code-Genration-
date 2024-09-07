import os

def generate_files(n):
    for i in range(1, n+1):
        with open(f'A{i}.txt', 'w') as f:
            f.write(f'{i}')
        with open(f'B{i}.txt', 'w') as f:
            f.write(f'{i}')
        with open(f'C{i}.txt', '