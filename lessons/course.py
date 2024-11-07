"""Review for QZ03"""


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self):
        self.make = "Honda"
        self.model = "CRV"
        self.year = 2020
        self.color = "Black"
        self.mileage = 22.3

    def update_mileage(self, miles: float) -> None:
        self.mileage = miles

    def display_info(self) -> None:
        print(
            f"This is a {self.color} {self.year} {self.make} {self.model} that gets {self.mileage} mpg"
        )
