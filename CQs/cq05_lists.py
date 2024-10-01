"""Mutating functions."""

__author__ = "730765267"


def manual_append(list: list[int], int: int) -> None:
    list.append(int)


def double(list: list[int]) -> None:
    count = 0
    while count < len(list):
        list[count] = list[count] * 2
        count += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
