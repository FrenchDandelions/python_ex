from S1E9 import Character


class Baratheon(Character):
    """ Representing the Baratheon family. """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize Baratheon object:
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """ Method that returns the object elements as a string """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Method returning the representation of the object elements as a string
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """(Baratheon) This function kills the character """
        if self.is_alive:
            self.is_alive = False
            # print(self.first_name, "died")
        # else:
            # print(self.first_name, "is already dead")


class Lannister(Character):
    """ Representing the Lannister family. """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize Lannister object:
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        """

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ Method to create new lannister object """
        return cls(first_name=first_name, is_alive=is_alive)

    def __str__(self):
        """ Method that returns the object elements as a string """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Method returning the representation of the object elements as a string
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """(Lannister) This function kills the character """
        if self.is_alive:
            self.is_alive = False
            # print(self.first_name, "died")
        # else:
            # print(self.first_name, "is already dead")
