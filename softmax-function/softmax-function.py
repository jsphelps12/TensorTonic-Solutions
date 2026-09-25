import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    if x.ndim == 1:
        adjusted = x - np.max(x)
        num = np.exp(adjusted)
        denom = np.sum(num)
        return num / denom
    adjusted = x - np.max(x, axis = 1, keepdims=True)
    num = np.exp(adjusted)
    denom = np.sum(num, axis = 1, keepdims=True)
    return num / denom
    pass