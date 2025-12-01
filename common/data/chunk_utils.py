from typing import Any, Iterable, List


def chunk_list(items: List[Any], chunk_size: int) -> Iterable[List[Any]]:
    """
    Yield lists of fixed size chunks.
    """
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]


def chunk_text(text: str, max_len: int) -> List[str]:
    """
    Split text into chunks of max length, preserving words.
    """
    words = text.split()
    chunks = []
    current = []

    for word in words:
        if sum(len(x) for x in current) + len(word) + len(current) > max_len:
            chunks.append(" ".join(current))
            current = [word]
        else:
            current.append(word)

    if current:
        chunks.append(" ".join(current))

    return chunks
