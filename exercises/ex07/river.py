"""File to define River class."""

__author__ = "730765267"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class definition."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages of fish and bears."""
        x: int = 0
        while x < len(self.fish):  # Checks ages of fish
            fish: Fish = self.fish[x]
            if fish.age > 3:
                self.fish.pop(x)
            else:
                x += 1
        y: int = 0
        while y < len(self.bears):  # Checks ages of bears
            bear: Bear = self.bears[y]
            if bear.age > 5:
                self.fish.pop(y)
            else:
                y += 1
        return None

    def bears_eating(self) -> None:
        """Bears eat and removes fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self) -> None:
        """Removes hungry bears."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def repopulate_fish(self) -> None:
        """Fish repopulate."""
        new_fish: int = (len(self.fish) // 2) * 4
        for x in range(0, new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Bears repopulate."""
        new_bears: int = len(self.bears) // 2
        for x in range(0, new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Prints river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """One week of life in river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes fish."""
        x: int = 0
        while x < amount:
            self.fish.pop(0)  # Removes first fish amount number of times
            x += 1
