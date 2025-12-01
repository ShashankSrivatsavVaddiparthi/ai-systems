import random
from typing import List, Tuple


def train_val_test_split(
    items: List, train_ratio=0.8, val_ratio=0.1, seed=42
) -> Tuple[List, List, List]:
    random.seed(seed)
    items = items.copy()
    random.shuffle(items)

    n = len(items)
    train_end = int(train_ratio * n)
    val_end = train_end + int(val_ratio * n)

    return items[:train_end], items[train_end:val_end], items[val_end:]
