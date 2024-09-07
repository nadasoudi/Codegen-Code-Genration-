import numpy as np

def multiply(poly, x):
    """Multiply a polynomial by a scalar.

    Args:
        poly (np.ndarray): A polynomial.
        x (float): A scalar.

    Returns:
        np.ndarray: The result of the multiplication.
    """
    return np.dot(poly, x)

def multiply_scalar(poly, x):
    """Multiply a polynomial by a scal