from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Function to load an image given the path"""
    try:
        if not isinstance(path, str):
            raise TypeError("Argument path must be a string")
        img = Image.open(path)
        arr = np.array(img)
        print("The shape of the image is:", arr.shape)
        print(arr[0:1])
        return arr

    except (TypeError, FileNotFoundError) as e:
        print(f"{type(e).__name__}{':'}", e)
    return []
