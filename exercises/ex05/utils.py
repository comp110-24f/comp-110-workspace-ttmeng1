"""Implementing list utility functions"""

__author__ = "730765267"


def only_evens(list1: list[int]) -> list[int]:
    """Returns a list of only even numbers"""
    idx: int = 0
    new_list: list[int] = []
    while idx < len(list1):
        if list1[idx] % 2 == 0:  # Checks if item is even
            new_list.append(list1[idx])  # Appends evens to new list
        idx += 1
    return new_list


def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Generates a subset of input list"""
    if (
        (len(list1) == 0) or (start >= len(list1)) or (end <= 0)
    ):  # Tests for cases that return empty list
        return []
    if start < 0:  # If start is negative, starts at beginning
        start = 0
    if end > len(list1):  # If end is greater than list length, ends with end
        end = len(list1)
    new_list: list[int] = []
    idx: int = 0
    while idx < len(list1):
        if (
            start <= idx < end
        ):  # When index is between start and end, adds item to new list
            new_list.append(list1[idx])
        idx += 1
    return new_list


def add_at_index(list1: list[int], element: int, index: int) -> None:
    if (index < 0) or (index > len(list1)):
        raise IndexError("Index is out of bounds for the input list")
    list1.append(0)  # Adds spacer to move items to right
    idx = len(list1) - 1
    while idx >= 0:
        if idx > index:
            list1[idx] = list1[idx - 1]  # Every item after desired index is moved down
        idx -= 1
    list1[index] = element  # Element is inserted at desired element
