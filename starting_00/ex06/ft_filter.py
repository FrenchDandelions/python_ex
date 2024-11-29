def ft_filter(f, obj):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if f:
        return iter([i for i in obj if f(i)])
    return iter([i for i in obj if i])
