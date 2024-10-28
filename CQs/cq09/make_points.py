from point import Point, scale

new_point: Point = Point(1, 2)
scale(new_point, 2)


def test_mutate() -> None:
    assert new_point.x == 1
    assert new_point.y == 2
