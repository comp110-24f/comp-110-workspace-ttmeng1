"""Practice functions for final exam."""


def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    """Determines if each game has enough points for free biscuits"""
    new_dict: dict[str, bool] = {}
    for game in games:
        sum: int = 0
        for point in games[game]:
            sum += point
        if sum >= 100:
            new_dict[game] = True
        else:
            new_dict[game] = False
    return new_dict


def max_key(vals: dict[str, list[int]]) -> str:
    """Returns name of key whose list has highest sum of values"""
    max: int = 0
    m_key: str = ""
    for key in vals:
        sum: int = 0
        for num in vals[key]:
            sum += num
        if sum >= max:
            max = sum
            m_key = key
    return m_key


def multiples(nums: list[int]) -> list[bool]:
    """Tells whether each value is a multiple of the previous value"""
    x: int = 0
    new_list: list[bool] = []
    while x < len(nums):
        if x == 0:
            if nums[0] % nums[len(nums) - 1] == 0:
                new_list.append(True)
            else:
                new_list.append(False)
            x += 1
        if nums[x] % nums[x - 1] == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        x += 1
    return new_list


def merge_lists(strs: list[str], ints: list[int]) -> dict[str, int]:
    """Maps item in first list to corresponding item in second"""
    new_dict: dict[str, int] = {}
    if len(strs) != len(ints):
        return new_dict
    x: int = 0
    while x < len(strs):
        new_dict[strs[x]] = ints[x]
        x += 1
    return new_dict


def reverse_multiply(nums: list[int]) -> list[int]:
    """Returns values doubled and in reverse order"""
    x: int = len(nums) - 1
    new_list: list[int] = []
    while x >= 0:
        new_list.append(nums[x] * 2)
        x -= 1
    return new_list


# Class writing
class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int
    ):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def calorie_count(self) -> float:
        cals: float = 0.0
        if self.flavor == "vanilla" or self.flavor == "peppermint":
            cals += 30
        cals += 20
        if self.has_whip is True:
            cals += 100
        cals += self.marshmallow_count / 2
        return cals


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        mins: int = self.minutes
        self.minutes = 0
        return mins

    def report(self) -> None:
        hours: int = self.minutes // 60
        minutes: int = self.minutes % 60
        print(
            f"{self.name} has spent {hours} hours and {minutes} minutes on {self.purpose}."
        )
