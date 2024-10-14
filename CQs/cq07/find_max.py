"""Defining function"""

__author__ = "730765267"


def find_and_remove_max(list: list[int]) -> int:
    """Identifies max int in list and removes it"""
    max: int = 0
    if len(list) == 0:
        return -1
    for item in list:
        if item > max:
            max = item
    idx: int = 0
    while idx < len(list):
        if list[idx] == max:
            list.pop(idx)
        else:
            idx += 1
    return max
