"""File to create Bear class."""

__author__ = "730765267"


class Bear:
    """Bear class"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes Bear"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Models one day for bear"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish) -> None:
        """Updates hunger score"""
        self.hunger_score += num_fish
