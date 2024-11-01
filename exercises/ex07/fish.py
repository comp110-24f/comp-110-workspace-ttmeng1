"""File to create Fish class."""

__author__ = "730765267"


class Fish:
    """Creates Fish class"""

    age: int

    def __init__(self):
        """Initializes Fish"""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Ages fish"""
        self.age += 1
