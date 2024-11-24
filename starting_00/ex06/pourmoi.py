class ft_filter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    def __init__(self, predicate, iterable):
        if predicate:
            self.predicate = predicate
        else:
            self.predicate = lambda x: bool(x)
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        elem = self.iterable.__next__()

        while not self.predicate(elem):
            elem = self.iterable.__next__()

        return elem
