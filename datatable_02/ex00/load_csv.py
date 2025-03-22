import pandas as pd


def load(path: str) -> pd.DataFrame:
    """This function takes a path as
argument, writes the dimensions of the
data set and returns said data set as
a panda data set. If the path is bad
or if the extension of the file is bad,
the function returns none.
The accepted extension is: '.csv'.
    """
    try:
        if not path.endswith(".csv"):
            return None
        dataset = pd.read_csv(path)
    except Exception as e:
        return None
        print(e)
    print("Loading dataset of dimensions", dataset.shape)
    return dataset


if __name__ == "__main__":
    print(load.__doc__)
    print(load("population_total.csv"))
