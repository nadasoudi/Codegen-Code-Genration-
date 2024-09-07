import numpy as np

def generate_3d_array(n):
    """
    Generate a 3D array of n elements.
    """
    return np.array([[np.random.randint(0, 10) for _ in range(3)] for _ in range(n)])

def main():
    """
    Run the program.
    """
    n = int(input("Enter the number of elements: "))
    print(gener