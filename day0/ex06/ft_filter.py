def ft_filter(func: any, iterable: any):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if (func is None):
        return (x for x in iterable if x)
    return (x for x in iterable if func(x))
