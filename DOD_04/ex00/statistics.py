def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Computes and prints statistical measures for a given set of numerical
        values.

    Parameters:
    *args (int | float): A variable-length list of numerical values.
    **kwargs (str): Keyword arguments specifying the statistical measures
                        to compute.
                    The valid keys and their corresponding measures are:
                        - 'toto': Mean
                        - 'tutu': Median
                        - 'tata': Quartiles (lower and upper)
                        - 'hello': Standard Deviation
                        - 'world': Variance

    Behavior:
    - If no arguments are provided or any argument is not a number,
        prints "ERROR".
    - If an invalid keyword argument is provided, prints "ERROR"
        for each invalid key.
    - If valid, prints the requested statistical measures.

    Example Usage:
    >>> ft_statistics(1, 2, 3, 4, toto='mean', tutu='median', tata='quartile')
    mean : 3.0
    median : 3
    quartile : [2.0, 4.0]

    Returns:
    None
    """
    err = None

    if not len(args):
        err = "ERROR"

    if any(not isinstance(i, (int, float)) for i in args):
        err = "ERROR"

    if err is not None:
        print(err)
        return

    c_dic = {
        'toto': 'mean',
        'tutu': 'median',
        'tata': 'quartile',
        'hello': 'std',
        'world': 'var'
    }

    if any(i not in c_dic or j is not c_dic[i] for i, j in kwargs.items()):
        a = sum(i not in c_dic or j is not c_dic[i] for i, j in kwargs.items())
        for i in range(a):
            print("ERROR")
        return

    def mean(lst):
        """Compute the arithmetic mean of a list of numbers."""
        return sum(lst) / len(lst)

    def c_median(lst):
        """Compute the median of a list of numbers."""
        s_list = sorted(lst)
        len_list = len(lst)
        mid = (len_list - 1) // 2
        if len_list % 2:
            median = s_list[mid]
        else:
            median = (s_list[mid] + s_list[mid + 1]) / 2.0
        return median

    def variance(lst):
        """Compute the variance of a list of numbers."""
        mu = mean(lst)
        return sum((x - mu) ** 2 for x in lst) / len(lst)

    def std(lst):
        """Compute the standard deviation of a list of numbers."""
        return variance(lst) ** .5

    if "toto" in kwargs.keys():
        print("mean :", mean(args))

    if "tutu" in kwargs.keys():
        print("median :", c_median(args))

    if "tata" in kwargs.keys():
        s_list = sorted(args)
        half_list = len(args) // 2 + 1
        lower_half = s_list[:half_list]
        upper_half = s_list[-half_list:]
        upper_quartile = float(c_median(upper_half))
        lower_quartile = float(c_median(lower_half))
        print("quartile :", [lower_quartile, upper_quartile])

    if "hello" in kwargs.keys():
        print("std :", std(args))

    if "world" in kwargs.keys():
        print("var :", variance(args))

    return
