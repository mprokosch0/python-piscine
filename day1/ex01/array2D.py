import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list):
            raise TypeError("family is not a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integers")
        arr = np.array(family)
        print("My shape is :", f"{arr.shape}")
        narr = arr[start:end]
        print("My new shape is :", f"{narr.shape}")
        return narr.tolist()

    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}{':'}", e)
    return []
