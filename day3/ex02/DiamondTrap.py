from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The king"""
    def set_eyes(self, color):
        """Method that updates the eyes color"""
        self.eyes = color

    def set_hairs(self, color):
        """Method that updates the hairs color"""
        self.hairs = color

    def get_eyes(self):
        """Method that return the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Method that return the hairs color"""
        return self.hairs
