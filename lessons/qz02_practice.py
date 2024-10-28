"""Practife functions for QZ02"""


# Write a function that will take a list[str] and returns a list[int]
#  of the size of each string in the input list.
def str_size(strings: list[str]) -> list[int]:
    sizes: list[int] = []
    for item in strings:
        sizes.append(len(item))
    return sizes


# Write a function that will take a list[str] and returns the sum of
# the lengths of all the strings.
def sum(strings: list[str]) -> int:
    total_sum: int = 0
    for item in strings:
        total_sum += len(item)
    return total_sum


# Write a function that will take a list[str] and mutates the list
# by adding a exclamation point to each string in the input list.
# Your function should not return anything.
def exclaim(strings: list[str]) -> None:
    for string in strings:
        string += "!"


# Write a function that takes a str input and returns a list with each
# element being a single character in the string input.
def str_to_list(string: str) -> list[str]:
    new_list: list[str] = []
    for char in string:
        new_list.append(char)
    return new_list


# Write a function that takes a int input and creates a list of the
# size of your input integer. Every element should be equal to their
# index value. When the function is called and finishes executing and
# the frame goes out of scope, the new list should still be avaiable
# for reference to a Global varibale.
def size_list(integer: int) -> list[int]:
    new_list: list[int] = []
    for num in range(0, integer):
        new_list.append(num)
    return new_list


# Write a function that take a list[float], an int, and a float and
# inserts the float into the list[float] at the index specified by
# the int passed to the function.
def insert_float(floats: list[float], integer: int, float: float) -> None:
    floats[integer] = float


# Write a function that takes a list[int] and returns a new list with
# only the even numbers.
def only_evens(nums: list[int]) -> list[int]:
    evens: list[int] = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


# Write a function that takes a list[str] and returns a new list with
# only the strings that contain the letter ‘a’.
def contains_a(string: list[str]) -> list[str]:
    a_strings: list[str] = []
    for item in string:
        if "a" in item:
            a_strings.append(item)
    return a_strings


# Write a function that takes a list[int] and returns the largest number.
def largest_numbers(nums: list[int]) -> int:
    max: int = 0
    for num in nums:
        if num > max:
            max = num
    return max


# Write a function that takes a str input and counts how many times
# of each vowel appears in the string and returns this as a summary
# in a dict[str, int].
def vowels(string: str) -> dict[str, int]:
    vowel_count: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for char in string:
        if char in vowel_count:
            vowel_count[char] += 1
    return vowel_count


# Write a function that takes two list[int] and returns a new list
# with the elements that appear in both lists.
def both_lists(list1: list[int], list2: list[int]) -> list[int]:
    new_list: list[int] = []
    for value in list1:
        if value in list2:
            new_list.append(value)
    return new_list


# Write a function that takes a list[float] and returns the average
# of the list, ignoring any negative numbers.
def average(nums: list[float]) -> float:
    sum_of_nums: float = 0
    count: int = 0
    for num in nums:
        if num >= 0:
            sum_of_nums += num
            count += 1
    average: float = sum_of_nums / count
    return average


# Write a function that takes a list[str] and returns a dictionary
# where the keys are the strings and the values are the lengths of
# each string.
def string_length(strings: list[str]) -> dict[str, int]:
    lengths: dict[str, int] = {}
    for string in strings:
        lengths[string] = len(string)
    return lengths


# Write a function that takes a str and returns a dict[str, int] that
# counts the frequency of each character in the string.
def char_frequency(string: str) -> dict[str, int]:
    frequency: dict[str, int] = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
