"""EX04: Utils!"""

__author__ = "730765267"


def all(list: list[int], int: int) -> bool:
    """Determines whether all ints in list are same as given int."""
    idx = 0
    if list == []:  # If list is empty, returns False
        return False
    while idx < len(list):
        if list[idx] != int:
            return False  # If value is not equal to integer, function exits
        idx += 1
    return True  # If all values are equal, function returns True


def max(list: list[int]) -> int:
    """Returns largest int in list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    idx = 0
    max = list[0]
    while idx < len(list):
        if max < list[idx]:
            max = list[idx]  # If value is larger than max, replaces existing max value
        idx += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if every element at every index is equal in 2 lists."""
    if len(list1) != len(list2):
        return False
    idx = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:  # If values are not equal anywhere, returns False
            return False
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates list by appending second list to end."""
    idx = 0
    while idx < len(
        list2
    ):  # Iterates through second list and appends every value to first list
        list1.append(list2[idx])
        idx += 1
