"""Dictionary Utility Functions"""

__author__ = "730765267"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    new_key: str = ""  # Creates empty value for key to add to a new dictionary
    new_val: str = ""  # Creates empty value for value that will be assigned to key
    new_dict: dict[str, str] = {}  # Empty dictionary for invertecd values
    no_double: list[str] = []  # List to store new key values to ensure they are unique
    for key in input:
        new_key = input[key]  # New key is old value
        new_val = key  # New value is old key
        if (
            new_key in no_double
        ):  # If the new key already exists in list, it is not unique and raises error
            raise KeyError("Dict cannot have two of the same key")
        no_double.append(new_key)
        new_dict[new_key] = new_val  # Appends inverted values to new dictionary
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most popular color in dictionary"""
    if colors == {}:
        return ""
    colors_count: dict[str, int] = (
        {}
    )  # Creates dictionary with color and how many times each appears
    for person in colors:
        if colors[person] in colors_count:
            colors_count[colors[person]] += 1
        else:
            colors_count[colors[person]] = 1
    colors_count_inverse: dict[int, str] = {}
    for color in colors_count:  # Inverts dictionary so count comes first
        new_key: int = colors_count[color]
        new_val: str = color
        colors_count_inverse[new_key] = new_val
    max: int = 0
    for count in colors_count_inverse:  # Finds largest count
        if count > max:
            max = count
    return colors_count_inverse[max]  # Returns color associated with largest count)


def count(list: list[str]) -> dict[str, int]:
    """Returns dictionary with how many times each item is in list"""
    dictionary: dict[str, int] = {}  # Empty dictionary to add counts to
    for item in list:
        if item in dictionary:
            dictionary[item] += 1  # If item is already in list, count goes up
        else:
            dictionary[item] = (
                1  # If item is not in list, adds to dictionary with value of 1
            )
    return dictionary


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Creates dictionary with letters and all words starting with letter"""
    dictionary: dict[str, list[str]] = {}
    for word in word_list:
        new_word = word.lower()  # Creates variable to store each word in all lower case
        first_letter = new_word[0]
        if (
            first_letter in dictionary
        ):  # If letter is already a key, adds word to the list of words
            letter_list: list[str] = dictionary[first_letter]
            letter_list.append(word)
        else:  # If letter is not in the dictionary, creates key
            dictionary[first_letter] = [word]
    return dictionary


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance log"""
    if day in attendance:  # If day is already logged, adds student to attendance record
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
