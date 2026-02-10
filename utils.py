from exceptions import DivisionByZeroError


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def flatten_list(data: list) -> list:
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed")
    return a / b


def count_words(sentence: str) -> dict:
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
