def square(x: int | float) -> int | float:
    """Function that returns the square of a number"""
    if not isinstance(x, (int, float)):
        raise TypeError("Value must be an integer or a float.")
    return x**2


def pow(x: int | float) -> int | float:
    """Function that returns the power of a number"""
    if not isinstance(x, (int, float)):
        raise TypeError("Value must be an integer or a float.")
    return x**x


def outer(x: int | float, function) -> object:
    """function that return a funtion that will increment itself"""
    count = 0

    def inner() -> float:
        """function that will be call severall times and will be
        incremented a bit each call"""
        try:
            nonlocal count
            count += 1
            res = x
            for i in range(count):
                res = function(res)
            return res
        except Exception as e:
            print(type(e).__name__ + ":", e)
    return inner
