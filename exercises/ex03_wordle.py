"""Exercise 3: Wordle"""

__author__ = "730765267"


def input_guess(secret_word_len: int) -> str:
    """Checks that guess word is correct length"""
    guess: str = input(f"Enter a {secret_word_len} character word:")
    while len(guess) != secret_word_len:  # Loops until input is correct length
        guess = input(f"That wasn't {secret_word_len} chars! Try again:")
    return guess  # Once out of while loop (guess is correct length), returns guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searches through secret word to see if it contains guessed character"""
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(
        secret_word
    ):  # Loops through each char in secret_word to see if it matches char_guess
        if secret_word[idx] == char_guess:
            return True
        else:
            idx += 1
    return False  # If no characters match at end of loop, returns False


def emojified(guess: str, secret_word: str) -> str:
    """Compares guess and secret_word and returns string of emojis"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    final_emoji: str = ""
    idx: int = 0
    while idx < len(secret_word):
        if (
            guess[idx] == secret_word[idx]
        ):  # Checks if letter is in same place and puts green box
            final_emoji = final_emoji + GREEN_BOX
        elif contains_char(
            secret_word=secret_word, char_guess=guess[idx]
        ):  # Checks if letter exists in secret word and puts yellow box
            final_emoji = final_emoji + YELLOW_BOX
        else:  # If letter is not in word at all, adds white box
            final_emoji = final_emoji + WHITE_BOX
        idx += 1
    return final_emoji


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    guesses: int = 1
    while guesses <= 6:  # Loops through to ask user for 6 guesses
        print(f"=== Turn {guesses}/6 ===")
        input_guess: str = input(f"Enter a {len(secret)} character word:")
        print(emojified(guess=input_guess, secret_word=secret))
        if emojified(guess=input_guess, secret_word=secret) == (
            "\U0001F7E9" * len(secret)
        ):  # If user guesses secret word correctly, loop exits
            print(f"You won in {guesses}/6 turns!")
            break
        else:
            guesses += 1
    if guesses == 7:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # If user does not guess in 6 guesses, game also ends


if __name__ == "__main__":
    main(secret="codes")
