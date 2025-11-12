import numpy as np


def inner1d(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return (arr1 * arr2).sum(axis=1)