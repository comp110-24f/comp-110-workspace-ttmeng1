"""Unit tests for list utility functions"""

__author__ = "730765267"

from utils import only_evens, sub, add_at_index


# Tests for only_evens
def test_evens_edge() -> None:
    """Tests edge case for only_evens"""
    assert only_evens([]) == []


def test_evens_return() -> None:
    """Tests return value for only_evens"""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_evens_mutate() -> None:
    """Ensures only_evens does not mutate original list"""
    a: list[int] = [1, 2, 3, 4, 5]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5]


# Tests for sub
def test_sub_edge() -> None:
    """Tests edge case for sub"""
    assert sub([1, 2], 1, -5) == []


def test_sub_return() -> None:
    """Ensures correct return value for sub"""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_sub_mutate() -> None:
    """Ensures sub does not mutate original list"""
    a: list[int] = [1, 2, 3, 4, 5]
    sub(a, 2, 4)
    assert a == [1, 2, 3, 4, 5]


# Tests for add_at_index
def test_add_edge() -> None:
    """Tests edge case for add_at_index"""
    a: list[int] = [1, 2, 3]
    add_at_index(a, 4, 0)
    assert a == [4, 1, 2, 3]


def test_add_return() -> None:
    """Ensures correct return value for add_at_index"""
    a: list[int] = [1, 3]
    add_at_index(a, 2, 1)
    assert a == [1, 2, 3]


def test_add_mutate() -> None:
    """Ensures add_at_index mutates original list"""
    a: list[int] = [1, 3]
    add_at_index(a, 2, 1)
    assert a != [1, 3]
