"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730765267"


def input_word() -> str:
    """Checks if input word is 5 letters"""
    guess: str = input("Enter a 5-character word: ")
    if len(guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Stops program if input is not 5 characters
    return guess  # Returns input only if it is correct


def input_letter() -> str:
    """Checks if input character is 1 character"""
    guess: str = input("Enter a single character: ")
    if len(guess) != 1:
        print("Error: Character must be a single character.")
        exit()  # Stops program if input is not a single character
    return guess


def contains_char(word: str, letter: str) -> None:
    """Puts everything together to find letter in word"""
    print("Searching for " + letter + " in " + word)
    count: int = 0  # Starts at 0 instances of letter in word
    if (
        letter == word[0]
    ):  # Multiple ifs so multiple conditions can be true at the same time
        print(letter + " found at index 0")
        count = count + 1  # Adds instance to count if letter is found
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(input_word(), input_letter())


if __name__ == "__main__":
    main()
