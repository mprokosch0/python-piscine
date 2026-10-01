
def callLimit(limit: int):
    """decorator function that takes a limit call to a function"""
    count = 0

    def callLimiter(function):
        """This function takes the function decorated as args"""

        def limit_function(*args: any, **kwds: any):
            """This function will test the actual amount of time
            of execution of a function"""
            try:
                if not isinstance(limit, int):
                    raise TypeError("limit should be an integer.")
                nonlocal count
                if (count >= limit):
                    print("Error :", function, "call too many times")
                else:
                    function(*args, **kwds)
                    count += 1
            except Exception as e:
                print(type(e).__name__ + ":", e)
        return limit_function
    return callLimiter
