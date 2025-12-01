import time
from datetime import datetime


def current_timestamp() -> str:
    """
    Return a human-friendly timestamp string.
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class Timer:
    """
    Context manager for timing code blocks.
    """

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
