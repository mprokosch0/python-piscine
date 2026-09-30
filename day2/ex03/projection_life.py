from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def format_nombre(x, pos):
    """function that formats numbers in plots"""
    if x >= 1_000_000_000:
        return f"{x/1_000_000_000:.1f}B"
    elif x >= 1_000_000:
        return f"{x/1_000_000:.1f}M"
    elif x >= 1_000:
        return f"{x/1_000:.0f}K"
    return f"{x:.0f}"


def main():
    life_expect = load("../life_expectancy_years.csv")
    income_per_pers = \
        load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    le1900 = life_expect["1900"]
    ipp1900 = income_per_pers["1900"]
    ax = plt.subplots()[1]
    ax.scatter(ipp1900, le1900)
    ax.set_xscale("log")
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life expectancy")
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_nombre))
    ax.set_title("1900")
    plt.show()


if __name__ == "__main__":
    main()
