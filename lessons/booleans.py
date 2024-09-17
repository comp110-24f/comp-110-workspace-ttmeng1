"""Practice with booleans"""


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hello", letter="h"))
print(check_first_letter(word="hello", letter="p"))
