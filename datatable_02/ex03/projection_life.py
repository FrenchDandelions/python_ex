from load_csv import load
import matplotlib.pyplot as plt
import matplotlib


def main() -> None:
    """ Main that displays the projection of life expectancy in relation to the
gross national product of the year 1900 for each country. """

    matplotlib.use('TkAgg')

    display_year = '1900'
    file_income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    dataframe_income = load(file_income)
    dataframe_expec = load("life_expectancy_years.csv")

    income_each_country = dataframe_income.loc[:, display_year]
    life_expec_each = dataframe_expec.loc[:, display_year]

    plt.scatter(income_each_country, life_expec_each)

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], labels=["300", "1000", "10k"])
    plt.xlim(300, 10000)

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title(display_year)

    plt.show()
    return None


if __name__ == "__main__":
    main()
