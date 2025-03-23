from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Diamond class King """
    def __init__(self, first_name, is_alive=True):
        """ Method to initiate King object """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """ Setter to modify obj.eyes elem """
        self.eyes = eyes
        return

    def set_hairs(self, hairs):
        """ Setter to modify obj.hairs elem """
        self.hairs = hairs
        return

    def get_eyes(self):
        """ Getter returning obj.eyes elem """
        return self.eyes

    def get_hairs(self):
        """ Getter returning obj.hairs elem """
        return self.hairs

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ Method to create new lannister object """
        obj = Lannister.create_lannister(first_name, is_alive)
        return obj

    def __str__(self):
        """ Method that returns the object elements as a string """
        return super().__str__()
