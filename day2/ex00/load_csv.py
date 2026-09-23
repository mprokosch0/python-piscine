import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Function that loads a csv from an argument Path
    and returns a DataFrame"""
    try:
        if not isinstance(path, str):
            raise TypeError("Argument path must be a string")
        table = pd.read_csv(path)
        print("Loading dataset of dimensions", table.shape)
        return table

    except (FileNotFoundError, TypeError, ValueError) as e:
        print(f"{type(e).__name__}{':'}", e)
    return None
