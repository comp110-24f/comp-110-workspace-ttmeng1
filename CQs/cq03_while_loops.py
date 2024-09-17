"""While loops challenge question"""

__author__ = "730765267"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns the count of occurences of search_char in prhase"""
    loop_count = 0
    char_count = 0
    while loop_count < len(phrase):
        if phrase[loop_count] == search_char:
            char_count += 1
    return char_count


print(num_instances(phrase="Hello", search_char="o"))
