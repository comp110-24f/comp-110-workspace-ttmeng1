"""Coordinates for CQ04"""

__author__ = "730765267"


def get_coords(xs: str, ys: str) -> None:
    idx_x = 0
    while idx_x < len(xs):
        a: str = ""
        b: str = ""
        a = xs[idx_x]
        idx_y = 0
        while idx_y < len(ys):
            b = ys[idx_y]
            print(f"({a}, {b})")
            idx_y += 1
        idx_x += 1
