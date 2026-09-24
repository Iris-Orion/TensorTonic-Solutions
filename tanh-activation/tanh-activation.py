import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x_arr = np.asarray(x, dtype=float)
    # return ( np.exp(x_arr) - np.exp(-x_arr) ) / ( np.exp(x_arr) + np.exp(-x_arr) )
    # return np.tanh(x)
    return np.sinh(x_arr) / np.cosh(x_arr)
    ret