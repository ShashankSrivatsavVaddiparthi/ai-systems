import time
from typing import Any, Callable


def retry(times: int = 3, delay: float = 1.0):
    """
    Retry a function call with optional delay.
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
                    time.sleep(delay)
            return None

        return wrapper

    return decorator
