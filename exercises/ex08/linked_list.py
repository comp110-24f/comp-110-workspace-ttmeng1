"""Linked list utils exercise."""

from __future__ import annotations

__author__ = "730765267"


class Node:
    """Node class definition."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Node to str magic method."""
        if self is None:
            return "None"
        else:
            rest: str = str(self.next)
            return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of the Node stored at the given index."""
    result: int = 0
    if head is None:  # If value of head is None, index is out of bounds
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:  # Returns value of current Node
        result = head.value
    else:  # Goes into next Node and decreases index by 1 until index is 0
        result = value_at(head.next, index - 1)
    return result


def max(head: Node | None) -> int:
    """Returns the maximum data value in the linked list."""
    if head is None:  # Empty linked list raises error
        raise ValueError("Cannot call max with None")
    max_value: int = head.value  # max_value is assigned value of whatever Node it is on
    if head.next is None:
        # If next is None, this is end of linked list and returns max_value
        return max_value
    else:
        if max_value <= max(head.next):
            # If value of current node is less than value of next node, max_value
            # becomes next Node's value
            max_value = head.next.value
        else:
            return max_value  # Otherwise, max_value remains value of current Node
    return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Returns linked list of Nodes with same values as input list."""
    if len(items) == 0:
        return None
    if len(items) == 1:  # Base case if list has only 1 item, returns that item and None
        return Node(items[0], None)
    else:
        first: int = items[0]  # Current first item in list
        rest: Node | None = linkify(items[1:])  # Recurs with list minus first item
        return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns new linked list of Nodes where each value is scaled by factor."""
    if head is None:  # If last Node in linked list, return None
        return None
    else:
        value: int = head.value * factor  # Scales current value by factor
        rest: Node | None = scale(
            head.next, factor
        )  # Recursive case, goes to next Node
        return Node(value, rest)
