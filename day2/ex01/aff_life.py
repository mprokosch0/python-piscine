from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load("../life_expectancy_years.csv")
        if data is None:
            raise
        france = data.loc[data['country'] == 'France']
        xaxis = france.columns.to_numpy()[1:]
        yaxis = france.to_numpy()[0][1:]
        plt.plot(xaxis, yaxis)
        plt.xticks(xaxis[::40])
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except (KeyboardInterrupt, ValueError,
            IndexError, KeyError, TypeError) as e:
        print(f"{type(e).__name__}{':'}", e)


if __name__ == "__main__":
    main()
