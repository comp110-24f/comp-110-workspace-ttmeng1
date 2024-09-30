"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# Adding items
my_numbers.append(1.5)

# initalizing populated list
game_points: list[int] = [102, 86, 94]

# indexing to print 94
print(game_points[2])

# replacing by index
game_points[1] = 72

# length of a list
print(len(game_points))

# removing an item from a list
game_points.pop(1)

# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over input and print every value


def display(input: list[int]) -> None:
    length = len(input)
    count = 0
    while count < length:
        print(input[count])
        count += 1


display(game_points)
