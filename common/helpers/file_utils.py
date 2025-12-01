from pathlib import Path
from typing import Union


def read_text(path: Union[str, Path], encoding="utf-8") -> str:
    path = Path(path)
    return path.read_text(encoding=encoding)


def write_text(path: Union[str, Path], text: str, encoding="utf-8") -> None:
    path = Path(path)
    path.parent.nkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding=encoding)
