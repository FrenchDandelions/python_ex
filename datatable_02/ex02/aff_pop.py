from load_csv import load
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter


def main() -> None:
    """Main that displays the country information of France versus Belgium"""
    matplotlib.use('TkAgg')

    dataframe = load("population_total.csv")

    frame_france = dataframe.loc[dataframe['country'] == "France"]
    frame_Belgium = dataframe.loc[dataframe['country'] == "Belgium"]

    years = dataframe.columns[1:].astype(int)

    values_france = frame_france.iloc[0, 1:].values
    values_france = [float(i[:-1]) for i in values_france]
    values_france = values_france[:250]
    values_belgium = frame_Belgium.iloc[0, 1:].values
    values_belgium = [float(i[:-1]) for i in values_belgium]
    values_belgium = values_belgium[:250]
    years = years[:250]

    plt.plot(years, values_france, label="France")
    plt.plot(years, values_belgium, label="Belgium")
    plt.xticks(range(years[0], 2051, 40))
    plt.xlim((years[0], 2050))

    max_val_y = int(max(max(values_france), max(values_belgium)))
    y_ticks = range(0, max_val_y, 20)
    plt.yticks(y_ticks)

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend(loc="lower right")

    def millions(x, pos):
        return f'{x:.0f}M'

    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))

    plt.show()
    return None


if __name__ == "__main__":
    main()
