class calculator:
    """This class contain 3 statics methods:
    
    -dotproduct

    -add_vec

    -sous_vec

    to see more print the __doc__ of each method"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """compute the dot product between 2 given vectors"""
        res = 0.0
        for i, num in enumerate(V1):
            res += num * V2[i]
        print("Dot product is:", int(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """compute an addition between each member of each vectors"""
        print("Add vector is:", [float(x) + float(y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """compute a soustraction between each member of each vectors"""
        print("Sous vector is:", [float(x) - float(y) for x, y in zip(V1, V2)])
