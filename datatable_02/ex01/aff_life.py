from load_csv import load
import matplotlib.pyplot as plt
import matplotlib


def main() -> None:
    """Main that loads the file life_expectancy_years.csv,
and displays the information of France"""
    matplotlib.use('TkAgg')

    dataframe = load("life_expectancy_years.csv")

    frame = dataframe.loc[dataframe['country'] == "France"]
    years = frame.columns[1:].astype(int)
    values = frame.iloc[0, 1:].values.astype(float)

    plt.plot(years, values)
    plt.xticks(range(years[0], years[-1] + 1, 40))

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.show()

    return None


if __name__ == "__main__":
    main()
