"""Recursion practice over a list."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    num_dogs: int = len(scores)
    if num_dogs <= idx:
        raise IndexError("Index is out of range")
    if int(scores[idx]["score"]) < thresh:
        return False
    elif idx == num_dogs - 1:
        return True
    else:
        return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
