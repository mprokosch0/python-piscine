class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0.0
        for i, num in enumerate(V1):
            res += num * V2[i]
        print("Dot product is:", int(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add vector is:", [float(x) + float(y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous vector is:", [float(x) - float(y) for x, y in zip(V1, V2)])
