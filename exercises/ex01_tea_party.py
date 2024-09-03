"""Program to plan a cozy tea party"""

__author__ = "730765267"


def main_planner(guests: int) -> None:
    """Prints output of other functions"""
    print("A cozy tea party for " + str(guests) + " people!")
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # Change int to str in order to concatenate
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # Calls tea_bags and treats as arguments for cost with guest are arugment for those functions


def tea_bags(people: int) -> int:
    """Returns number of tea bags based on number of people"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats based on cups of tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns total cost based on amount of tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
