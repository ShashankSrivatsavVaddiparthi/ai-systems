import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning: strip, remove extra spaces, normalize whitespace.
    """
    return re.sub(r"\s+", " ", text.strip())


def tokenize(text: str) -> list[str]:
    """
    Naive tokenization: split on whitespace.
    """
    return clean_text(text).split(" ")
