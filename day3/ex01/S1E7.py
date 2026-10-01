from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "Dark"

    def die(self):
        """Method that makes the Character die"""
        self.is_alive = False

    def __str__(self):
        """baratheon __str__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """baratheon __repr__"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "Light"

    def die(self):
        """Method that makes the Character die"""
        self.is_alive = False

    def __str__(self):
        """Lannister __str__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Lannister __repr__"""
        return self.__str__()

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """Class method that create a Lannister"""
        return self(first_name, is_alive)
