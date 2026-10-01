
def mean(lst: list) -> None:
    """Calculate the mean value of a list and prints the it"""
    res = 0
    for x in lst:
        res += x
    res = res / len(lst)
    print("mean :", res)


def median(lst: list) -> None:
    """Calculate the median value of a list and prints the it"""
    if (len(lst) % 2):
        print("median :", lst[int((len(lst)) / 2)])
    else:
        print("median :", (lst[(len(lst) - 1) / 2] + lst[(len(lst)) / 2]) / 2)


def quartile(lst: list) -> None:
    """Calculate the quartiles values of a list and prints them"""
    res = [float(lst[int((len(lst)-1)*0.25)]),
           float(lst[int((len(lst)-1)*0.75)])]
    print("quartile :", res)


def std(lst: list) -> None:
    """Calculate the standart deviation of a list and print it"""
    moy = 0
    for x in lst:
        moy += x
    moy = moy / len(lst)
    sum = 0
    for x in lst:
        sum += (x - moy)**2
    sum /= len(lst)
    sum = sum**0.5
    print("std :", sum)


def var(lst: list) -> None:
    """Calculate the variance of a list and print it"""
    moy = 0
    for x in lst:
        moy += x
    moy = moy / len(lst)
    sum = 0
    for x in lst:
        sum += (x - moy)**2
    sum /= len(lst)
    print("var :", sum)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """takes a list of value and a dictionnary and
    calculate for the given list differents values
    stored inside the dictionnary.
    The possible values in the dictionnary are:
    -mean
    -median
    -quartile
    -std (standard deviation)
    -var (variance)
    """
    try:
        lst = [x for x in args]
        lst.sort()
        for key in kwargs:
            val = kwargs[key]
            if len(args) == 0 and val in {"mean", "median",
                                          "quartile", "std", "var"}:
                print("ERROR")
            elif val == "mean":
                mean(lst)
            elif val == "median":
                median(lst)
            elif val == "quartile":
                quartile(lst)
            elif val == "std":
                std(lst)
            elif val == "var":
                var(lst)
    except TypeError as e:
        print(TypeError.__name__ + ":", e)
