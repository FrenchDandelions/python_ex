class calculator:
    """ This is a calculator class to do calculations """
    def __init__(self, elem):
        """ Method that Initialize the calculator, takes list as param """
        self.elem = elem
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Static method to do the dot product of 2 vectors """
        a = sum(a * b for a, b in zip(V1, V2))
        print(a)
        return

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ Static method to do the addition of 2 vectors """
        a = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", a)
        return

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ Static method to do the substraction of 2 vectors """
        a = [float(a - b) for a, b in zip(V1, V2)]
        print("Sous Vector is:", a)
        return
