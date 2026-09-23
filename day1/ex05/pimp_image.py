import numpy as np


def ft_invert(arr: np.array) -> np.array:
    """Inverts the color of the image received."""
    return 255 - arr.copy()


def ft_red(arr: np.array) -> np.array:
    """Convert the image in red colors"""
    arr = arr.copy()
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    return arr


def ft_green(arr: np.array) -> np.array:
    """Convert the image in green colors"""
    arr = arr.copy()
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    return arr


def ft_blue(arr: np.array) -> np.array:
    """Convert the image in blue colors"""
    arr = arr.copy()
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    return arr


def ft_grey(arr: np.array) -> np.array:
    """Convert the image in gray colors"""
    arr = arr.copy()
    arr = np.dot(arr[:, :, :3], [0.21256, 0.7174, 0.0721])
    return arr
