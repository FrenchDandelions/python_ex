def ft_statistics(*args: any, **kwargs: any) -> None:

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
        return sum(lst) / len(lst)

    def c_median(lst):
        s_list = sorted(lst)
        len_list = len(lst)
        mid = (len_list - 1) // 2
        if len_list % 2:
            median = s_list[mid]
        else:
            median = (s_list[mid] + s_list[mid + 1]) / 2.0
        return median

    def variance(lst):
        mu = mean(lst)
        return sum((x - mu) ** 2 for x in lst) / len(lst)

    def std(lst):
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
