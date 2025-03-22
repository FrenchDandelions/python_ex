from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f'({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        return f'({self.family_name}, {self.eyes}, {self.hairs})'


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"


    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name=first_name, is_alive=is_alive)


    def __str__(self):
        return f'({self.family_name}, {self.eyes}, {self.hairs})'
    
    def __repr__(self):
        return f'({self.family_name}, {self.eyes}, {self.hairs})'
