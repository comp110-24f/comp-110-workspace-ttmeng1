"""Unit tests"""

__author__ = "730765267"

from find_max import find_and_remove_max


def test_return() -> None:
    """Ensures find_and_remove_max returns expected value"""
    assert find_and_remove_max([1, 2, 3, 4, 5]) == 5


def test_mutate() -> None:
    """Ensures find_and_remove_max mutates input as expected"""
    a: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4]


def test_edge() -> None:
    """Tests edge case"""
    a: list[int] = [5, 5, 5, 5, 5]
    find_and_remove_max(a)
    assert a == []
