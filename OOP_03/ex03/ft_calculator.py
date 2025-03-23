class calculator:
    """ This is a calculator class to do calculations """
    def __init__(self, elem):
        """ Method that Initialize the calculator, takes list as param """
        self.elem = elem
        pass

    def __add__(self, object) -> None:
        """ Method to add to all elems of the calculator """
        self.elem = [i + object for i in self.elem]
        print(self.elem)
        return

    def __mul__(self, object) -> None:
        """ Method to multiply to all elems of the calculator """
        self.elem = [i * object for i in self.elem]
        print(self.elem)
        return

    def __sub__(self, object) -> None:
        """ Method to substract to all elems of the calculator """
        self.elem = [i - object for i in self.elem]
        print(self.elem)
        return

    def __truediv__(self, object) -> None:
        """ Method to divide to all elems of the calculator """
        if not object:
            print("Can't divide by 0")
            return
        self.elem = [i / object for i in self.elem]
        print(self.elem)
        return
