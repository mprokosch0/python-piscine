from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def toNum(arr: np.array) -> np.array:
    """Translate pop literals to numbers"""
    res = []

    for x in range(arr.shape[0]):
        if arr[x][-1] == 'k':
            res.append(float(arr[x][:-1]) * 1_000)
        elif arr[x][-1] == 'M':
            res.append(float(arr[x][:-1]) * 1_000_000)
        elif arr[x][-1] == 'B':
            res.append(float(arr[x][:-1]) * 1_000_000_000)
        else:
            res.append(float(arr[x]))
    return np.array(res)


def format_nombre(x, pos):
    if x >= 1_000_000_000:
        return f"{x/1_000_000_000:.1f}B"
    elif x >= 1_000_000:
        return f"{x/1_000_000:.1f}M"
    elif x >= 1_000:
        return f"{x/1_000:.0f}K"
    return f"{x:.0f}"


def main():
    try:
        data = load("../population_total.csv")
        if data is None:
            raise
        france = data.loc[data["country"] == "France"]
        xFra = france.columns.to_numpy()[1:252]
        yFra = france.to_numpy()[0][1:252]

        Thailand = data.loc[data["country"] == "Thailand"]
        xThai = Thailand.columns.to_numpy()[1:252]
        yThai = Thailand.to_numpy()[0][1:252]

        yFra = toNum(yFra)
        yThai = toNum(yThai)

        ax = plt.subplots()[1]

        ax.plot(xThai, yThai, label="Thaïlande", color="blue")
        ax.plot(xFra, yFra, label="France", color="green")
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.set_xticks(xFra[::40])
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_nombre))
        plt.legend(loc=4)
        plt.show()
    except (KeyboardInterrupt, ValueError,
            IndexError, KeyError, TypeError) as e:
        print(f"{type(e).__name__}{':'}", e)


if __name__ == "__main__":
    main()
