import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function that generate an random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """dataclass that represents a student"""
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """post constructor"""
        self.login = self.name[0] + self.surname
