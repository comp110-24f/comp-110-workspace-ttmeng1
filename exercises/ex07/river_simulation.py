"""File for river simulation."""

__author__ = "730765267"

from river import River

my_river: River = River(num_fish=10, num_bears=2)


my_river.view_river()
my_river.one_river_week()