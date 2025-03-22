from abc import ABC, abstractclassmethod


class Character(ABC):
    """This is a Character class that takes as parameter
a string (first_name) and a boolean (is_alive)"""
    def __init__(self, first_name, is_alive=True):
        """This function is called to initialize a Character Object """
        self.first_name = first_name
        self.is_alive = is_alive
        super().__init__()
        
    def die(self):
        """This function kills the character """
        if self.is_alive :
            self.is_alive = False
            print(self.first_name, "died")
        else:
            print(self.first_name, "is already dead")


class Stark(Character):
    """This is a Stark class that inherits from the
Character class"""
    def __init__(self, first_name, is_alive=True):
        """This function is called to initialize a Stark Object
and call the constructor of the Character object which it inherits"""
        super().__init__(first_name, is_alive)