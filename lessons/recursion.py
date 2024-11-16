from __future__ import annotations

"""Linked list recursion practice"""


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self):
        if self is None:
            return "None"
        else:
            rest: str = str(self.next)
            return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    """Return alst value of linked list"""
    if head.next is None:
        return head.value  # Base case
    else:
        return last(head.next)  # Recursive case


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list from start up until end"""
    if start > end:
        raise Exception("Invalid use of recursive range")
    if start == end:
        return None
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)
