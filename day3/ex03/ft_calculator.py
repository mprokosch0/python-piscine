class calculator:
    """Defines a calculator class which supports the following operators:

    -addition (+)
    -substraction (-)
    -multiplication (*)
    -divition (/)
    """
    def __init__(self, object) -> None:
        self.vector = [x for x in object]

    def __add__(self, object) -> None:
        """Apply an addition through the object"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Apply an substraction through the object"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Apply an multiplication through the object"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Apply an division through the object"""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(ZeroDivisionError.__name__ + ":", e)
